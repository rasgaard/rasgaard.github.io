#!/usr/bin/env python3
"""Bespoke local markdown editor for rasgaard.com (Jekyll on GitHub Pages).

Run:  python3 editor/server.py  (or: make editor)
Open: http://localhost:8001

Stdlib only — no pip install needed.
"""
import base64
import datetime
import json
import mimetypes
import os
import re
import subprocess
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # repo root
HERE = Path(__file__).resolve().parent
PORT = int(os.environ.get("EDITOR_PORT", "8001"))

COLLECTIONS = {
    "phd_status": ROOT / "_phd_status",
    "blog": ROOT / "_blog",
}
PAGES = [
    {"label": "Home (index.md)", "path": "index.md"},
    {"label": "PhD index (phd/index.md)", "path": "phd/index.md"},
    {"label": "Blog index (blog/index.md)", "path": "blog/index.md"},
]
ATTACHMENTS = ROOT / "assets" / "attachments"


# ---------- frontmatter helpers (tiny YAML subset: title/layout/date/tags) ----------

def split_frontmatter(text):
    """Return (fm_dict, body). fm_dict has title/layout/date/tags(raw str)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    fm = {}
    # simple line-based parse; keep tags block as raw lines
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        kv = re.match(r"^(\w+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            if key == "tags" and (val == "" or val is None):
                tags = []
                i += 1
                while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                    tags.append(re.sub(r"^\s*-\s+", "", lines[i]).strip())
                    i += 1
                fm["tags"] = tags
                continue
            fm[key] = val
        i += 1
    return fm, body


def build_file(title, layout, date, tags, body, published=True):
    tags = tags or []
    out = ["---", f"title: {title}", f"layout: {layout or 'default'}"]
    if date:
        out.append(f"date: {date}")
    if tags:
        out.append("tags:")
        out.extend(f"  - {t}" for t in tags)
    if not published:
        out.append("published: false")
    out.append("---")
    body = body or ""
    if body and not body.startswith("\n"):
        out.append("")
    out.append(body.rstrip("\n") + "\n" if body else "")
    return "\n".join(out)


def safe_path(rel):
    """Resolve rel against ROOT, rejecting escapes and editor internals."""
    p = (ROOT / rel).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise ValueError("path escapes repo")
    if p == ROOT:
        raise ValueError("invalid path")
    return p


def allowed_edit_path(rel):
    p = safe_path(rel)
    rp = str(p.relative_to(ROOT))
    if rp.startswith(("_phd_status/", "_blog/", "phd/index.md", "blog/index.md", "index.md")):
        return p
    raise ValueError("only _phd_status, _blog and index pages are editable")


def list_files():
    data = {"phd_status": [], "blog": [], "pages": []}
    for key, d in COLLECTIONS.items():
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            try:
                text = f.read_text()
            except OSError:
                continue
            fm, _ = split_frontmatter(text)
            data[key].append({
                "path": str(f.relative_to(ROOT)),
                "name": f.name,
                "title": fm.get("title", f.stem),
                "date": fm.get("date", ""),
                "published": str(fm.get("published", "true")).lower() != "false",
            })
        # newest first by date string (YYYY-MM-DD sorts fine); fallback name
        data[key].sort(key=lambda e: (e["date"] or e["name"]), reverse=True)
    for pg in PAGES:
        p = ROOT / pg["path"]
        entry = {"label": pg["label"], "path": pg["path"], "exists": p.exists()}
        if p.exists():
            fm, _ = split_frontmatter(p.read_text())
            entry["title"] = fm.get("title", pg["label"])
        data["pages"].append(entry)
    return data


def run_git(args, timeout=60):
    r = subprocess.run(["git"] + args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    return r


def git_status_payload():
    status = run_git(["status", "--short", "--branch"]).stdout.strip()
    log = run_git(["log", "--oneline", "-5"]).stdout.strip()
    # ahead/behind parse from branch line e.g. ## main...origin/main [ahead 1]
    return {"status": status, "log": log}


# ---------- HTTP ----------

class Handler(BaseHTTPRequestHandler):
    server_version = "SiteEditor/1.0"

    def log_message(self, fmt, *args):
        pass  # quiet

    def _send(self, code, body, ctype="application/json"):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj), "application/json")

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        if not length:
            return {}
        return json.loads(self.rfile.read(length) or b"{}")

    # -- routes --
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path, qs = parsed.path, urllib.parse.parse_qs(parsed.query)

        if path in ("/", "/index.html"):
            self._send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
            return
        if path == "/api/files":
            try:
                self._json(list_files())
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return
        if path == "/api/file":
            rel = (qs.get("path") or [""])[0]
            try:
                p = allowed_edit_path(rel)
                if not p.exists():
                    self._json({"error": "not found"}, 404)
                    return
                fm, body = split_frontmatter(p.read_text())
                tags = fm.get("tags", [])
                if isinstance(tags, str):
                    tags = [tags]
                self._json({
                    "path": rel, "title": fm.get("title", ""),
                    "layout": fm.get("layout", "default"),
                    "date": fm.get("date", ""),
                    "tags": tags, "body": body,
                    "published": str(fm.get("published", "true")).lower() != "false",
                })
            except ValueError as e:
                self._json({"error": str(e)}, 403)
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return
        if path == "/api/git/status":
            try:
                self._json(git_status_payload())
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return
        if path.startswith("/assets/"):
            # serve site assets (images, css) so the preview looks like the site
            try:
                p = safe_path(urllib.parse.unquote(path.lstrip("/")))
                if not p.is_file():
                    self._send(404, "not found", "text/plain")
                    return
                ctype, _ = mimetypes.guess_type(str(p))
                self._send(200, p.read_bytes(), ctype or "application/octet-stream")
            except ValueError:
                self._send(403, "forbidden", "text/plain")
            except Exception as e:
                self._send(500, str(e), "text/plain")
            return
        self._send(404, "not found", "text/plain")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/save":
            try:
                d = self._read_json()
                rel = d.get("path", "")
                p = allowed_edit_path(rel)
                title = (d.get("title") or p.stem).strip()
                layout = (d.get("layout") or "default").strip()
                date = (d.get("date") or "").strip()
                tags = d.get("tags") or []
                if isinstance(tags, str):
                    tags = [t.strip() for t in tags.split(",") if t.strip()]
                body = d.get("body") or ""
                published = d.get("published", True)
                if isinstance(published, str):
                    published = published.lower() not in ("false", "no", "0")
                # PhD updates conventionally start with "# {{ page.title }}"
                if rel.startswith("_phd_status/") and not p.exists() and body and not body.lstrip().startswith("#"):
                    body = "# {{ page.title }}\n\n" + body
                if rel.startswith("_blog/") and not p.exists() and body and not body.lstrip().startswith("#"):
                    body = "# {{ page.title }}\n\n" + body
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(build_file(title, layout, date, tags, body, published))
                self._json({"ok": True, "path": rel})
            except ValueError as e:
                self._json({"error": str(e)}, 403)
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return

        if path == "/api/upload":
            # JSON: {docPath, filename, dataUrl} — dataUrl is data:<mime>;base64,...
            try:
                d = self._read_json()
                doc_path = d.get("docPath", "")
                allowed_edit_path(doc_path)  # validate scope
                slug = Path(doc_path).stem
                filename = re.sub(r"[^A-Za-z0-9._-]+", "-", d.get("filename") or "pasted.png").strip("-") or "pasted.png"
                data_url = d.get("dataUrl", "")
                m = re.match(r"^data:([^;]+);base64,(.*)$", data_url, re.DOTALL)
                if not m:
                    self._json({"error": "expected a data: URL image"}, 400)
                    return
                mime, b64 = m.group(1), m.group(2)
                ext = mimetypes.guess_extension(mime.split(";")[0]) or ""
                if ext in (".jpe",):
                    ext = ".jpg"
                # ensure filename has an image extension
                if not re.search(r"\.(png|jpe?g|gif|webp|svg|avif)$", filename, re.I):
                    filename += ext or ".png"
                # avoid collisions: prefix timestamp if exists
                dest_dir = ATTACHMENTS / slug
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest = dest_dir / filename
                if dest.exists():
                    stem, suffix = dest.stem, dest.suffix
                    dest = dest_dir / f"{stem}-{int(time.time())}{suffix}"
                dest.write_bytes(base64.b64decode(b64))
                url = f"/assets/attachments/{slug}/{dest.name}"
                self._json({"ok": True, "url": url, "markdown": f"![]({url})"})
            except ValueError as e:
                self._json({"error": str(e)}, 403)
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return

        if path == "/api/git":
            try:
                d = self._read_json()
                action = d.get("action")
                if action == "pull":
                    r = run_git(["pull", "--ff-only"])
                    self._json({"ok": r.returncode == 0, "output": (r.stdout + r.stderr).strip()})
                elif action == "push":
                    r = run_git(["push"])
                    self._json({"ok": r.returncode == 0, "output": (r.stdout + r.stderr).strip()})
                elif action == "commit":
                    msg = (d.get("message") or "").strip() or f"site update {datetime.date.today().isoformat()}"
                    a = run_git(["add", "-A", "--", "_phd_status", "_blog", "phd", "blog", "index.md", "assets"])
                    if a.returncode != 0:
                        self._json({"ok": False, "output": a.stderr.strip()})
                        return
                    # nothing to commit?
                    s = run_git(["status", "--porcelain", "--", "_phd_status", "_blog", "phd", "blog", "index.md", "assets"]).stdout.strip()
                    if not s:
                        self._json({"ok": True, "output": "nothing to commit"})
                        return
                    c = run_git(["commit", "-m", msg])
                    self._json({"ok": c.returncode == 0, "output": (c.stdout + c.stderr).strip()})
                else:
                    self._json({"error": "unknown action"}, 400)
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return

        self._send(404, "not found", "text/plain")


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Editor running at http://localhost:{PORT}  (repo: {ROOT})")
    print("Press Ctrl+C to stop.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass

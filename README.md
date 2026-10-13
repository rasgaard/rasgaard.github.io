# rasgaard.github.io

Jekyll source for https://rasgaard.com.

## Stack / build

- Jekyll 4.3 + kramdown (`Gemfile`, `_config.yml`). Plugins: `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag`.
- Commands (`Makefile`): `make install`, `make serve` (dev server), `make build` (`bundle exec jekyll build`), `make clean`, `make editor` (local md editor on :8001).
- `editor/` is local tooling only, excluded from the site in `_config.yml`.
- Domain: `CNAME` → rasgaard.com. `404.html`, `robots.txt` at root.
- Home: `index.md` (layout `default`, bio + bluesky embed).

## Layouts & styling

- `_layouts/default.html`: single site chrome. Nav: PhD `/phd/`, Blog `/blog/`, Projects `/projects/`. Loads `/assets/css/style.css` always; Prism (code highlight) only if `tags` contains `code`; KaTeX + auto-render only if `tags` contains `math`.
- `_layouts/post.html` exists but unused — all content uses `layout: default`.
- Title pattern: `<title>{{ page.title }} | {{ site.title }}</title>`.

## Collections (source → list page → URL)

Defined in `_config.yml` under `collections:` with `output: true`:

| Source dir | List page | Permalink | Purpose |
|---|---|---|---|
| `_blog/` | `blog/index.md` | `/blog/:name/` | Long-form posts |
| `_projects/` | `projects/index.md` | `/projects/:name/` | Project archive with status filter |
| `_phd_status/` | `phd/index.md` (+ About text) | `/phd/status/:name/` | Monthly PhD updates |

List pages sort `site.<collection>` by `date` reversed. `projects/index.md` renders filterable cards (`all/ongoing/finished/idea/dropped`) via `status` frontmatter + `summary` + formatted date. `blog/index.md` and `phd/index.md` render simple `- YYYY, Month - <title>` lists.

## Frontmatter conventions

### `_projects/<slug>.md`
```yaml
---
title: Short human title
layout: default
date: YYYY-MM-DD  # use exact date if known (e.g. 2023-07-16), else month-end
status: ongoing | finished | idea | dropped  # must match a filter pill in projects/index.md
summary: One sentence, plain language, for the card grid.
---
```
Body convention (see `_projects/msc-thesis.md`, `whisper-encoder-pruning.md`):
`# {{ page.title }}` then `## Goal` (why it matters, newcomer-friendly) then `## Report` (how it went, links, images).

### `_blog/<slug>.md`
```yaml
---
title: Post title
date: YYYY-MM-DD
layout: default
tags:
  - post
  - code  # optional: enables Prism
  - math  # optional: enables KaTeX
---
```
Body starts with `# {{page.title}}`. Images go in `assets/attachments/<slug>/` and are referenced as `/assets/attachments/<slug>/file.png`. Interactive figures in `assets/embeds/*.html`.

### `_phd_status/YYYY-month.md`
```yaml
---
title: Month title
layout: default
date: YYYY-MM-DD  # month-end
tags:
  - status
---
```
Body starts with `# {{ page.title }}`, free-form sections.

## Assets

- `assets/css/style.css` — all site CSS (incl. `.proj-grid`, `.proj-card`, `.pill-*`, `.filter-bar`).
- `assets/attachments/<project-or-post-slug>/image.png` — per-item images, e.g. `thesis/`, `whisper-encoder-pruning/`, `local-coding-agents/`.
- `assets/embeds/*.html` — standalone interactive embeds.

## How to add content

- **Project:** create `_projects/<slug>.md` with the frontmatter above + Goal/Report body. It appears automatically on `/projects/`. Date controls sort order (newest first).
- **Blog post:** create `_blog/<slug>.md` with frontmatter above. Appears on `/blog/`.
- **PhD update:** create `_phd_status/YYYY-month.md`. Appears on `/phd/`.
- Always run `make build` to verify (Jekyll must exit `done`, no warnings about missing frontmatter).

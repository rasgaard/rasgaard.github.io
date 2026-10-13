---
layout: default
title: Projects
---

# Projects

An archive of things I've built, am building, want to build, or stopped building.

My driving interests are **model compression** (quantization, pruning, distillation) and **on-device AI deployment**: squeezing capable models onto hardware with limited compute, especially where privacy, latency, or cost rule out the cloud. If something here overlaps with what you're working on, or you have a half-baked idea in the same space, [reach out](https://www.linkedin.com/in/rasgaard/). I'm always up for comparing notes or collaborating.

<div class="filter-bar" id="filters">
  <a class="filter-btn" href="#all" data-f="all">All</a>
  <a class="filter-btn" href="#ongoing" data-f="ongoing">On-going</a>
  <a class="filter-btn" href="#finished" data-f="finished">Finished</a>
  <a class="filter-btn" href="#idea" data-f="idea">Ideas</a>
  <a class="filter-btn" href="#dropped" data-f="dropped">Dropped</a>
</div>

<div class="proj-grid">
{% assign items = site.projects | sort: 'date' | reverse %}
{% for p in items %}
  <div class="proj-card" data-status="{{ p.status }}">
    <span><span class="pill pill-{{ p.status }}">{{ p.status }}</span></span>
    <h2><a href="{{ p.url }}">{{ p.title }}</a></h2>
    {% if p.summary %}<p>{{ p.summary }}</p>{% endif %}
    <div class="proj-meta">{{ p.date | date: '%B %Y' }}</div>
  </div>
{% endfor %}
</div>

<script>
(function () {
  var valid = ['all', 'ongoing', 'finished', 'idea', 'dropped'];
  function apply() {
    var f = (location.hash || '#all').slice(1);
    if (valid.indexOf(f) === -1) f = 'all';
    document.querySelectorAll('#filters .filter-btn').forEach(function (b) {
      b.classList.toggle('active', b.dataset.f === f);
    });
    document.querySelectorAll('.proj-card').forEach(function (c) {
      c.style.display = (f === 'all' || c.dataset.status === f) ? '' : 'none';
    });
  }
  window.addEventListener('hashchange', apply);
  apply();
})();
</script>

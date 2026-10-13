---
layout: default
title: Blog
---

# Blog posts

{% assign posts = site.blog | sort: 'date' | reverse %}
{% for status in posts %}
   - {{status.date | date: '%Y'}}, **{{status.date | date: '%B'}}** - <a href="{{status.url}}">{{status.title}}</a>
{% endfor %}
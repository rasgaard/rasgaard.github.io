---
layout: default
title: PhD Status
---

# Status Updates

{% assign posts = site.phd_status | sort: 'date' | reverse %}
{% for status in posts %}
   - {{status.date | date: '%Y'}}, **{{status.date | date: '%B'}}** - <a href="{{status.url}}">{{status.title}}</a>
{% endfor %}
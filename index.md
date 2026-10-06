---
layout: default
title: Lecture Notes
---

# Lecture Notes

Browse the notes below. Each Markdown file is rendered as a page on this site.

{% assign markdown_pages = site.pages | where_exp: "page", "page.name contains '.md'" | sort: "name" %}
{% for markdown_page in markdown_pages %}
{% unless markdown_page.name == "index.md" %}
- [{{ markdown_page.name | remove: ".md" | replace: "_", " " }}]({{ markdown_page.url | relative_url }})
{% endunless %}
{% endfor %}

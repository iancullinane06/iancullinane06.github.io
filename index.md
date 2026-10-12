---
layout: default
title: Lecture Notes
---

# Lecture Notes

Browse the notes below. Each Markdown file is rendered as a page on this site.

<label for="lecture-search">Search lecture topics and notes</label>
<input id="lecture-search" type="search" placeholder="e.g. heat capacity" aria-controls="lecture-list" aria-describedby="lecture-search-status">
<p id="lecture-search-status" role="status" aria-live="polite"></p>

<ul id="lecture-list">
{% assign markdown_pages = site.pages | where_exp: "page", "page.name contains '.md'" | sort: "name" %}
{% for markdown_page in markdown_pages %}
{% unless markdown_page.name == "index.md" %}
<li data-search-content="{{ markdown_page.content | normalize_whitespace | escape }}"><a href="{{ markdown_page.url | relative_url }}">{{ markdown_page.name | remove: ".md" | replace: "_", " " }}</a></li>
{% endunless %}
{% endfor %}
</ul>

<script src="{{ '/assets/js/lecture-search.js' | relative_url }}" defer></script>

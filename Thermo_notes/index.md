---
layout: default
title: Lecture Notes
---

# Thermodynamics lecture notes

Explore the lectures and study summary below. Use the navigation on the left to move between lectures, and open the definitions tab for a quick reference.

<label for="lecture-search">Search lecture topics and notes</label>
<input id="lecture-search" type="search" placeholder="e.g. heat capacity" aria-controls="lecture-list" aria-describedby="lecture-search-status">
<p id="lecture-search-status" role="status" aria-live="polite"></p>

<ul id="lecture-list">
{% assign markdown_pages = site.pages | where_exp: "p", "p.path contains 'Thermo_notes/'" | where_exp: "p", "p.name contains '.md'" | sort: "nav_order" %}
{% for markdown_page in markdown_pages %}
{% unless markdown_page.name == "index.md" %}
<li data-search-content="{{ markdown_page.name | append: ' ' | append: markdown_page.content | escape }}"><a href="{{ markdown_page.url | relative_url }}">{{ markdown_page.title | default: markdown_page.name | remove: ".md" | replace: "_", " " }}</a></li>
{% endunless %}
{% endfor %}
<li data-search-content="Lecture 23 PDF"><a href="{{ '/Lecture_23.pdf' | relative_url }}">Lecture 23 (PDF)</a></li>
</ul>

<script src="{{ '/assets/js/lecture-search.js' | relative_url }}" defer></script>

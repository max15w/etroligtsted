---
title: "Reading Log"
layout: readinglog
excerpt: "Et Roligt Sted - Reading Log"
sitemap: false
permalink: /readinglog.html
---


<html lang="en">
<head>
<style>
  .reading-log { max-width: 1100px; margin: 0 auto; padding: 0 1rem; color:#111; }
  .year-heading { font-size: 40px; margin: 2rem 0 1rem; border-bottom: 2px solid #ccc; padding-bottom: 4px; }

  .reading-grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(120px, 1fr));
    gap: 18px 20px;
  }
  @media (max-width: 1100px) { .reading-grid { grid-template-columns: repeat(5, 1fr); } }
  @media (max-width: 900px)  { .reading-grid { grid-template-columns: repeat(4, 1fr); } }
  @media (max-width: 720px)  { .reading-grid { grid-template-columns: repeat(3, 1fr); } }
  @media (max-width: 520px)  { .reading-grid { grid-template-columns: repeat(2, 1fr); } }

  .book { text-align: center; }

  .book-image {
    width: 150px; height: 220px; object-fit: cover;
    border: 2px solid grey; border-radius: 5px; padding: 2px; background: #f7f7f7;
    margin: 0 auto; display: block;
  }
  .star-rating {
    font-size: 20px; margin-top: 10px;
    display: flex; justify-content: center; gap: 2px;
  }
  .star-rating .full  { color: grey; }
  .star-rating .half  {
    background: linear-gradient(to right, grey 50%, #fff 50%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .star-rating .empty { color: #ccc; }
</style>

<div class="reading-log">
  {%- assign items = site.data.readinglog | default: empty -%}
  {%- if items == empty or items.size == 0 -%}
    <p>No entries yet.</p>
  {%- else -%}
    {%- assign grouped = items | group_by: "year" -%}
    {%- assign grouped_sorted = grouped | sort: "name" | reverse -%}
    {%- for g in grouped_sorted -%}
      <h2 class="year-heading">{{ g.name }}</h2>
      <div class="reading-grid">
        {%- for entry in g.items -%}
          {%- assign img = entry.image -%}
          {%- if img and img contains '://' -%}
            {%- assign src = img -%}
          {%- else -%}
            {%- assign src = site.baseurl | append: img -%}
          {%- endif -%}

          {%- assign rating_num = entry.rating | default: 0 | plus: 0 -%}
          {%- assign r10 = rating_num | times: 10 | round: 0 -%}
          {%- assign half_mod = r10 | modulo: 10 -%}
          {%- if half_mod == 5 -%}{% assign half_star = 1 %}{% else %}{% assign half_star = 0 %}{% endif %}
          {%- assign full_stars = rating_num | floor -%}
          {%- assign next_after_full = full_stars | plus: 1 -%}

          <figure class="book">
            <img class="book-image" src="{{ src }}" alt="Book cover">
            <div class="star-rating" aria-label="{{ rating_num }} out of 5">
              {% for i in (1..5) %}
                {% if i <= full_stars %}
                  <span class="full">★</span>
                {% elsif half_star == 1 and i == next_after_full %}
                  <span class="half">★</span>
                {% else %}
                  <span class="empty">☆</span>
                {% endif %}
              {% endfor %}
            </div>
          </figure>
        {%- endfor -%}
      </div>
    {%- endfor -%}
  {%- endif -%}
</div>



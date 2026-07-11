---
title: "Reading Log"
layout: readinglog
excerpt: "Arkivet - Reading Log"
sitemap: false
permalink: /readinglog.html
---

<style>
  @font-face {
    font-family: "CustomFont";
    src: url("{{ '/fonts/Rons.ttf' | relative_url }}") format("truetype");
    font-weight: 400;
    font-style: normal;
    font-display: swap;
  }

  :root {
    --page-background: #F7F4EE;
    --paper: #FCFBF8;
    --ink: #302E2C;
    --line: #DDD9D0;

    --sage-tab: #B8BDA9;
    --sage-header: #D9DECF;
    --sage-accent: #A8AE9B;
    --sage-hover: #E9EDE4;

    --blue-tab: #B0B4B7;
    --blue-header: #D8DDE0;
    --blue-accent: #9FA6AE;
    --blue-hover: #E9EDF0;

    --peach-tab: #C7B0A1;
    --peach-header: #E4D4CA;
    --peach-accent: #C8A38F;
    --peach-hover: #F2E9E3;

    --olive-tab: #C8C2B1;
    --olive-header: #E3DED2;
    --olive-accent: #B8B396;
    --olive-hover: #F0EEE7;

    --star-empty: #D8D6CE;
  }

  body {
    background: var(--page-background) !important;
    background-image: none !important;
    color: var(--ink);
    font-family: "CustomFont", Georgia, serif;
  }

  .reading-log-page {
    width: 100%;
    margin: 0 auto;
    font-family: "CustomFont", Georgia, serif;
  }

  .reading-log-title {
    margin: 8px auto 82px;

    font-family: "CustomFont", Georgia, serif;
    font-size: clamp(5rem, 9vw, 9.5rem);
    font-weight: normal;
    font-style: normal;
    line-height: 1;
    letter-spacing: 0.015em;

    color: var(--ink);
    text-align: center;
  }

  .year-section {
    position: relative;
    margin-bottom: 92px;
    padding-top: 42px;
  }

  .year-tab {
    position: absolute;
    top: 0;
    left: 38px;
    z-index: 2;

    display: flex;
    align-items: center;
    justify-content: center;

    height: 56px;
    padding: 0 32px;
    border-radius: 17px 17px 0 0;
  }

  .year-tab-title {
    display: block;

    font-family: "CustomFont", Georgia, serif;
    font-size: clamp(1.9rem, 2.3vw, 2.7rem);
    font-weight: normal;
    font-style: normal;
    line-height: 1;
    letter-spacing: 0.01em;

    color: var(--ink);
    white-space: nowrap;
  }

  .year-panel {
    padding: 38px 34px 34px;
    border-top: 1px solid var(--line);
  }

  /* Year colour themes */

  .year-sage .year-tab {
    background: var(--sage-tab);
  }

  .year-sage .year-panel {
    background: linear-gradient(
      180deg,
      rgba(184, 189, 169, 0.22) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .year-sage .book-cover-wrap {
    border-color: rgba(168, 174, 155, 0.58);
  }

  .year-sage .book-cover-wrap:hover {
    background: var(--sage-hover);
  }

  .year-sage .star-rating .full,
  .year-sage .star-rating .half {
    color: #7F8774;
  }

  .year-blue .year-tab {
    background: var(--blue-tab);
  }

  .year-blue .year-panel {
    background: linear-gradient(
      180deg,
      rgba(176, 180, 183, 0.25) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .year-blue .book-cover-wrap {
    border-color: rgba(159, 166, 174, 0.58);
  }

  .year-blue .book-cover-wrap:hover {
    background: var(--blue-hover);
  }

  .year-blue .star-rating .full,
  .year-blue .star-rating .half {
    color: #7E8790;
  }

  .year-peach .year-tab {
    background: var(--peach-tab);
  }

  .year-peach .year-panel {
    background: linear-gradient(
      180deg,
      rgba(199, 176, 161, 0.25) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .year-peach .book-cover-wrap {
    border-color: rgba(200, 163, 143, 0.58);
  }

  .year-peach .book-cover-wrap:hover {
    background: var(--peach-hover);
  }

  .year-peach .star-rating .full,
  .year-peach .star-rating .half {
    color: #A27B6C;
  }

  .year-olive .year-tab {
    background: var(--olive-tab);
  }

  .year-olive .year-panel {
    background: linear-gradient(
      180deg,
      rgba(200, 194, 177, 0.30) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .year-olive .book-cover-wrap {
    border-color: rgba(184, 179, 150, 0.58);
  }

  .year-olive .book-cover-wrap:hover {
    background: var(--olive-hover);
  }

  .year-olive .star-rating .full,
  .year-olive .star-rating .half {
    color: #8F8B70;
  }

  .reading-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
    gap: 30px 24px;
  }

  .book {
    margin: 0;
    text-align: center;
  }

  .book-cover-wrap {
    display: block;
    padding: 10px;

    background: var(--paper);
    border: 1px solid;
    border-radius: 16px;

    transition:
      transform 0.18s ease,
      background-color 0.18s ease,
      box-shadow 0.18s ease;
  }

  .book-cover-wrap:hover {
    box-shadow: 0 8px 18px rgba(80, 80, 70, 0.10);
    transform: translateY(-3px);
  }

  .book-image {
    display: block;
    width: 100%;
    aspect-ratio: 2 / 3;

    object-fit: cover;
    border-radius: 10px;
    background: #EEE9E0;
  }

  .star-rating {
    display: flex;
    justify-content: center;
    gap: 3px;
    margin-top: 11px;

    font-family: Arial, sans-serif;
    font-size: 1.12rem;
    line-height: 1;
  }

  .star-rating .half {
    background: linear-gradient(
      to right,
      currentColor 50%,
      var(--star-empty) 50%
    );

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;
    color: transparent;
  }

  .star-rating .empty {
    color: var(--star-empty);
  }

  .empty-reading-log {
    padding: 28px;

    border: 1px solid var(--line);
    border-radius: 14px;
    background: var(--paper);

    font-family: "CustomFont", Georgia, serif;
    font-size: 1.15rem;
  }

  @media (max-width: 900px) {
    .reading-grid {
      grid-template-columns: repeat(auto-fill, minmax(145px, 1fr));
      gap: 24px 18px;
    }
  }

  @media (max-width: 700px) {
    .reading-log-title {
      margin-bottom: 60px;
      font-size: clamp(4rem, 15vw, 7rem);
    }

    .year-section {
      margin-bottom: 66px;
      padding-top: 36px;
    }

    .year-tab {
      left: 20px;
      height: 48px;
      padding: 0 24px;
      border-radius: 14px 14px 0 0;
    }

    .year-tab-title {
      font-size: clamp(1.5rem, 5vw, 2.1rem);
    }

    .year-panel {
      padding: 30px 10px 10px;
    }

    .reading-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 22px 14px;
    }

    .book-cover-wrap {
      padding: 7px;
      border-radius: 12px;
    }

    .book-image {
      border-radius: 8px;
    }
  }
</style>

<div class="reading-log-page" markdown="0">

  <h1 class="reading-log-title">Reading Log</h1>

  {%- assign items = site.data.readinglog | default: empty -%}

  {%- if items == empty or items.size == 0 -%}

    <div class="empty-reading-log">
      No entries yet.
    </div>

  {%- else -%}

    {%- assign grouped = items | group_by: "year" -%}
    {%- assign grouped_sorted = grouped | sort: "name" | reverse -%}

    {%- for g in grouped_sorted -%}

      {% assign colour_index = forloop.index0 | modulo: 4 %}

      {% if colour_index == 0 %}
        {% assign year_colour = "year-sage" %}
      {% elsif colour_index == 1 %}
        {% assign year_colour = "year-blue" %}
      {% elsif colour_index == 2 %}
        {% assign year_colour = "year-peach" %}
      {% else %}
        {% assign year_colour = "year-olive" %}
      {% endif %}

      <section class="year-section {{ year_colour }}">

        <div class="year-tab">
          <span class="year-tab-title">{{ g.name }}</span>
        </div>

        <div class="year-panel">
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

              {%- if half_mod == 5 -%}
                {%- assign half_star = 1 -%}
              {%- else -%}
                {%- assign half_star = 0 -%}
              {%- endif -%}

              {%- assign full_stars = rating_num | floor -%}
              {%- assign next_after_full = full_stars | plus: 1 -%}

              <figure class="book">

                <a
                  class="book-cover-wrap"
                  href="{{ src }}"
                  target="_blank"
                  rel="noopener"
                  aria-label="Open book cover">

                  <img
                    class="book-image"
                    src="{{ src }}"
                    alt="Book cover">

                </a>

                <div
                  class="star-rating"
                  aria-label="{{ rating_num }} out of 5">

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
        </div>

      </section>

    {%- endfor -%}

  {%- endif -%}

</div>
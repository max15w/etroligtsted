---
title: "Gallery"
layout: doodleddiary
excerpt: "Et Roligt Sted - Gallery"
sitemap: false
permalink: /gallery.html
---

<html lang="en">
<head>
<style>
  /* ========= Pinterest-style masonry board (no JS) ========= */
  .board {
    column-gap: 1rem;
    column-count: 3;     /* ALWAYS 3 columns */
    padding: .25rem 0 0;
  }

  /* Optional: make it usable on very small screens */
  @media (max-width: 700px) {
    .board { column-count: 1; }
  }

  /* ========= pin/card ========= */
  .pin {
    break-inside: avoid;
    -webkit-column-break-inside: avoid;
    margin: 0 0 1rem 0;

    border-radius: 12px;
    overflow: hidden;
    background: rgba(255,255,255,0.80);
    box-shadow: 0 4px 16px rgba(0,0,0,.08);

    display: block;
    width: 100%;
  }

  /* Defensive reset against theme rules that commonly break captions/layout */
  .pin, .pin * { box-sizing: border-box; }
  .pin figure { margin: 0 !important; padding: 0 !important; }
  .pin figure,
  .pin img {
    position: static !important;
    transform: none !important;
    filter: none !important;
    opacity: 1 !important;
  }

  /* ========= image ========= */
  .pin__img {
    width: 100%;
    height: auto;
    display: block;
    max-width: 100%;
  }

  /* ========= caption ========= */
  .pin__caption {
    display: block;
    position: relative;
    z-index: 2;

    padding: .65rem .85rem .85rem;
    background: rgba(255,255,255,.92);
    color: #222 !important;
    line-height: 1.25;
    font-size: 1.3rem;

    text-shadow: none !important;
    mix-blend-mode: normal !important;
  }

  .pin:hover { box-shadow: 0 8px 24px rgba(0,0,0,.12); }
</style>

{%- assign raw = site.data.gallery.items | default: site.data.gallery -%}

{%- comment -%}
Sort by DD/MM/YY from YAML without changing gallery.yml.
Build sortable tokens like "2025-11-05|||INDEX".
{%- endcomment -%}
{%- assign tokens = "" | split: "" -%}
{%- for it in raw -%}
  {%- assign parts = it.date | split: "/" -%}
  {%- assign dd = parts[0] | strip -%}
  {%- assign mm = parts[1] | strip -%}
  {%- assign yy = parts[2] | strip -%}

  {%- if dd.size == 1 -%}{%- assign dd = "0" | append: dd -%}{%- endif -%}
  {%- if mm.size == 1 -%}{%- assign mm = "0" | append: mm -%}{%- endif -%}

  {%- assign yyyy = yy -%}
  {%- if yyyy.size == 2 -%}
    {%- assign yyyy = "20" | append: yyyy -%}
  {%- endif -%}

  {%- assign sortkey = yyyy | append: "-" | append: mm | append: "-" | append: dd -%}
  {%- assign token = sortkey | append: "|||" | append: forloop.index0 -%}
  {%- assign tokens = tokens | push: token -%}
{%- endfor -%}

{%- assign tokens = tokens | sort | reverse -%}

<div class="board">
  {%- for t in tokens -%}
    {%- assign bits = t | split: "|||" -%}
    {%- assign idx = bits[1] | plus: 0 -%}
    {%- assign it = raw[idx] -%}

    <article class="pin">
      <figure>
        <img
          src="{{ it.src | escape }}"
          alt="{{ it.alt | default: it.caption | escape }}"
          class="pin__img"
          loading="lazy">
        <div class="pin__caption">{{ it.caption }}</div>
      </figure>
    </article>
  {%- endfor -%}
</div>

</head>
</html>

---
title: "Gallery"
layout: doodleddiary
excerpt: Arkivet - Gallery"
sitemap: false
permalink: /gallery.html
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

    --panel-start: #E8E8DF;
    --panel-mid: #F0EEE6;
    --panel-end: #F7F4EE;

    --card-background: rgba(252, 251, 248, 0.9);
    --card-background-hover: rgba(255, 255, 255, 0.96);

    --ink: #302E2C;
    --muted-ink: rgba(48, 46, 44, 0.62);

    --line: #DDD9D0;
    --card-line: rgba(255, 255, 255, 0.96);

    --card-shadow: rgba(70, 62, 52, 0.07);
    --card-shadow-hover: rgba(70, 62, 52, 0.12);

    --caption-font: Georgia, "Times New Roman", Times, serif;
  }

  body {
    background: var(--page-background) !important;
    background-image: none !important;
    color: var(--ink);
    font-family: "CustomFont", Georgia, serif;
  }

  .gallery-page {
    width: min(1760px, calc(100% - 24px));
    margin: 0 auto;
    padding: 0 0 80px;
  }

  .gallery-title {
    display: block;
    width: 100%;
    margin: 0 auto 30px;

    font-family: "CustomFont", Georgia, serif;
    font-size: clamp(5rem, 9vw, 9.5rem);
    font-weight: normal;
    line-height: 1;
    letter-spacing: 0.015em;

    color: var(--ink);
    text-align: center;
  }

  .gallery-panel {
    width: 100%;
    margin: 0 auto;

    background:
      linear-gradient(
        135deg,
        var(--panel-start) 0%,
        var(--panel-mid) 50%,
        var(--panel-end) 100%
      );

    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    border-left: none;
    border-right: none;
    border-radius: 0;

    padding: 22px 12px 26px;
    box-sizing: border-box;
  }

  .board {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    grid-auto-rows: 8px;
    gap: 10px 8px;
    align-items: start;
  }

  .pin {
    display: block;
    width: 100%;

    overflow: hidden;
    border-radius: 18px;

    background: var(--card-background);
    border: 1px solid var(--card-line);

    box-shadow: 0 5px 14px var(--card-shadow);

    padding: 6px;
    box-sizing: border-box;

    transition:
      transform 180ms ease,
      background-color 180ms ease,
      box-shadow 180ms ease;
  }

  .pin:hover {
    transform: translateY(-2px);
    background: var(--card-background-hover);
    box-shadow: 0 8px 18px var(--card-shadow-hover);
  }

  .pin,
  .pin * {
    box-sizing: border-box;
  }

  .pin figure {
    display: flex !important;
    flex-direction: column !important;
    margin: 0 !important;
    padding: 0 !important;

    position: static !important;
    transform: none !important;
    filter: none !important;
    opacity: 1 !important;
  }

  .pin__link {
    display: block !important;
    width: 100%;

    margin: 0 !important;
    padding: 0 !important;

    color: inherit;
    text-decoration: none;
    cursor: zoom-in;
  }

  .pin__link:hover,
  .pin__link:focus {
    color: inherit;
    text-decoration: none;
  }

  .pin__img {
    display: block !important;
    width: 100%;
    max-width: 100%;
    height: auto;

    margin: 0 !important;
    padding: 0 !important;

    position: static !important;
    transform: none !important;
    filter: none !important;
    opacity: 1 !important;

    border-radius: 11px;
    background: #EEE9E0;
  }

  .pin__caption {
    display: block !important;
    position: static !important;
    transform: none !important;

    width: 100%;
    margin: 0 !important;
    padding: 0.46rem 0.18rem 0.02rem !important;

    clear: both;

    background: transparent !important;
    border-top: none;

    color: var(--ink) !important;

    font-family: var(--caption-font);
    font-size: 0.95rem;
    font-weight: 600;
    line-height: 1.18;

    text-align: center;
    text-shadow: none !important;
    mix-blend-mode: normal !important;
  }

  .pin__date {
    display: block;
    margin-top: 0.16rem;

    color: var(--muted-ink);
    font-family: var(--caption-font);
    font-size: 0.8rem;
    font-weight: 400;
    line-height: 1.1;
  }

  .gallery-lightbox {
    position: fixed;
    inset: 0;
    z-index: 5000;

    display: none;
    align-items: center;
    justify-content: center;

    padding: 42px;

    background: rgba(247, 244, 238, 0.94);
    backdrop-filter: blur(6px);
  }

  .gallery-lightbox.is-open {
    display: flex;
  }

  .gallery-lightbox-inner {
    position: relative;

    width: min(1150px, 94vw);
    max-height: 92vh;

    display: flex;
    flex-direction: column;

    overflow: hidden;
    border-radius: 22px;

    background: rgba(252, 251, 248, 0.98);
    border: 1px solid var(--card-line);

    box-shadow: 0 22px 60px rgba(45, 38, 32, 0.22);
  }

  .gallery-lightbox-image-wrap {
    display: flex;
    align-items: center;
    justify-content: center;

    min-height: 0;
    padding: 14px;
    background: rgba(252, 251, 248, 0.98);
  }

  .gallery-lightbox-image {
    display: block;
    width: auto;
    height: auto;

    max-width: 100%;
    max-height: calc(92vh - 135px);

    object-fit: contain;
    border-radius: 14px;
    background: #EEE9E0;
  }

  .gallery-lightbox-caption {
    display: block;
    padding: 0.8rem 1.2rem 1rem;

    background: rgba(252, 251, 248, 0.98);
    border-top: 1px solid var(--line);

    color: var(--ink);

    font-family: var(--caption-font);
    font-size: 1.05rem;
    font-weight: 600;
    line-height: 1.35;
    text-align: center;
  }

  .gallery-lightbox-date {
    display: block;
    margin-top: 0.25rem;

    color: var(--muted-ink);
    font-family: var(--caption-font);
    font-size: 0.92rem;
    font-weight: 400;
  }

  .gallery-lightbox-close {
    position: absolute;
    top: 12px;
    right: 12px;
    z-index: 2;

    width: 36px;
    height: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    border: 1px solid var(--line);
    border-radius: 999px;
    background: rgba(252, 251, 248, 0.9);

    color: var(--ink);
    font-family: var(--caption-font);
    font-size: 1.35rem;
    line-height: 1;

    cursor: pointer;
  }

  .gallery-lightbox-close:hover {
    background: #EEE9E0;
  }

  @media (max-width: 1240px) {
    .gallery-page {
      width: min(100% - 20px, 1760px);
    }

    .board {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }
  }

  @media (max-width: 850px) {
    .gallery-page {
      width: min(100% - 18px, 1760px);
    }

    .gallery-panel {
      padding: 16px 8px 20px;
    }

    .board {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px 6px;
    }

    .pin {
      padding: 5px;
      border-radius: 16px;
    }

    .pin__img {
      border-radius: 10px;
    }
  }

  @media (max-width: 560px) {
    .gallery-page {
      width: min(100% - 12px, 1760px);
      padding-bottom: 52px;
    }

    .gallery-title {
      margin-bottom: 22px;
      font-size: clamp(4rem, 15vw, 7rem);
    }

    .gallery-panel {
      padding: 12px 6px 16px;
    }

    .board {
      grid-template-columns: 1fr;
      gap: 8px;
    }

    .pin {
      padding: 5px;
      border-radius: 16px;
    }

    .pin__caption {
      font-size: 0.96rem;
    }

    .pin__date {
      font-size: 0.84rem;
    }

    .gallery-lightbox {
      padding: 18px;
    }

    .gallery-lightbox-inner {
      width: 96vw;
      max-height: 94vh;
      border-radius: 20px;
    }

    .gallery-lightbox-image-wrap {
      padding: 10px;
    }

    .gallery-lightbox-image {
      max-height: calc(94vh - 130px);
      border-radius: 12px;
    }
  }
</style>

{%- assign raw = site.data.gallery.items | default: site.data.gallery -%}
{%- assign tokens = "" | split: "" -%}

{%- for it in raw -%}
  {%- assign parts = it.date | split: "/" -%}
  {%- assign dd = parts[0] | strip -%}
  {%- assign mm = parts[1] | strip -%}
  {%- assign yy = parts[2] | strip -%}

  {%- if dd.size == 1 -%}
    {%- assign dd = "0" | append: dd -%}
  {%- endif -%}

  {%- if mm.size == 1 -%}
    {%- assign mm = "0" | append: mm -%}
  {%- endif -%}

  {%- assign yyyy = yy -%}
  {%- if yyyy.size == 2 -%}
    {%- assign yyyy = "20" | append: yyyy -%}
  {%- endif -%}

  {%- assign sortkey = yyyy | append: "-" | append: mm | append: "-" | append: dd -%}
  {%- assign token = sortkey | append: "|||" | append: forloop.index0 -%}
  {%- assign tokens = tokens | push: token -%}
{%- endfor -%}

{%- assign tokens = tokens | sort | reverse -%}

<div class="gallery-page" markdown="0">

  <h1 class="gallery-title">Gallery</h1>

  <div class="gallery-panel">

    <div class="board" aria-label="Gallery">

      {%- for t in tokens -%}
        {%- assign bits = t | split: "|||" -%}
        {%- assign idx = bits[1] | plus: 0 -%}
        {%- assign it = raw[idx] -%}

        <article class="pin">
          <figure>

            <a
              class="pin__link"
              href="{{ it.src | relative_url | escape }}"
              data-full-src="{{ it.src | relative_url | escape }}"
              data-alt="{{ it.alt | default: it.caption | escape }}"
              data-caption="{{ it.caption | escape }}"
              data-date="{{ it.date | escape }}"
              aria-label="Open larger gallery image">

              <img
                src="{{ it.src | relative_url | escape }}"
                alt="{{ it.alt | default: it.caption | escape }}"
                class="pin__img"
                loading="lazy"
                decoding="async">

            </a>

            {%- if it.caption or it.date -%}
              <figcaption class="pin__caption">
                {%- if it.caption -%}
                  {{ it.caption }}
                {%- endif -%}

                {%- if it.date -%}
                  <span class="pin__date">{{ it.date }}</span>
                {%- endif -%}
              </figcaption>
            {%- endif -%}

          </figure>
        </article>

      {%- endfor -%}

    </div>

  </div>

</div>

<div
  class="gallery-lightbox"
  id="galleryLightbox"
  aria-hidden="true">

  <div class="gallery-lightbox-inner" role="dialog" aria-modal="true">
    <button
      class="gallery-lightbox-close"
      type="button"
      aria-label="Close larger image">
      ×
    </button>

    <div class="gallery-lightbox-image-wrap">
      <img
        class="gallery-lightbox-image"
        id="galleryLightboxImage"
        src=""
        alt="">
    </div>

    <div class="gallery-lightbox-caption">
      <span id="galleryLightboxCaptionText"></span>
      <span class="gallery-lightbox-date" id="galleryLightboxDate"></span>
    </div>
  </div>

</div>

<script>
  (function () {
    function initGalleryLightbox() {
      var lightbox = document.getElementById("galleryLightbox");
      var lightboxImage = document.getElementById("galleryLightboxImage");
      var captionText = document.getElementById("galleryLightboxCaptionText");
      var captionDate = document.getElementById("galleryLightboxDate");
      var closeButton = document.querySelector(".gallery-lightbox-close");

      if (!lightbox || !lightboxImage || !captionText || !captionDate) {
        return;
      }

      function openLightbox(link) {
        var src = link.getAttribute("data-full-src") || link.getAttribute("href");
        var alt = link.getAttribute("data-alt") || "";
        var caption = link.getAttribute("data-caption") || "";
        var date = link.getAttribute("data-date") || "";

        if (!src) {
          return;
        }

        lightboxImage.src = src;
        lightboxImage.alt = alt;
        captionText.textContent = caption;
        captionDate.textContent = date;

        lightbox.classList.add("is-open");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
      }

      function closeLightbox() {
        lightbox.classList.remove("is-open");
        lightbox.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";

        lightboxImage.src = "";
        lightboxImage.alt = "";
        captionText.textContent = "";
        captionDate.textContent = "";
      }

      document.querySelectorAll(".pin__link").forEach(function (link) {
        link.addEventListener("click", function (event) {
          event.preventDefault();
          openLightbox(link);
        });
      });

      if (closeButton) {
        closeButton.addEventListener("click", closeLightbox);
      }

      lightbox.addEventListener("click", function (event) {
        if (event.target === lightbox) {
          closeLightbox();
        }
      });

      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && lightbox.classList.contains("is-open")) {
          closeLightbox();
        }
      });
    }

    function initMasonry() {
      var board = document.querySelector(".board");
      var pins = document.querySelectorAll(".pin");

      if (!board || pins.length === 0) {
        return;
      }

      function resizeMasonryItem(pin) {
        var rowHeight = parseInt(window.getComputedStyle(board).getPropertyValue("grid-auto-rows"), 10);
        var rowGap = parseInt(window.getComputedStyle(board).getPropertyValue("row-gap"), 10);
        var pinHeight = pin.getBoundingClientRect().height;
        var rowSpan = Math.ceil((pinHeight + rowGap) / (rowHeight + rowGap));
        pin.style.gridRowEnd = "span " + rowSpan;
      }

      function resizeAllMasonryItems() {
        pins.forEach(function (pin) {
          resizeMasonryItem(pin);
        });
      }

      resizeAllMasonryItems();

      document.querySelectorAll(".pin__img").forEach(function (img) {
        if (img.complete) {
          resizeAllMasonryItems();
        } else {
          img.addEventListener("load", resizeAllMasonryItems);
        }
      });

      window.addEventListener("resize", resizeAllMasonryItems);
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () {
        initGalleryLightbox();
        initMasonry();
      });
    } else {
      initGalleryLightbox();
      initMasonry();
    }
  })();
</script>
---
title: "Library"
layout: library
excerpt: "Arkivet - Library"
sitemap: false
permalink: /library.html
---

<link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">

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
    --paper-soft: #FCFBF8;
    --line: #DDD9D0;
    --line-dark: #D0CAB8;
    --ink: #302E2C;
    --table-font: Georgia, "Times New Roman", Times, serif;

    /* books: muted sage */
    --books-tab: #B8BDA9;
    --books-panel: #F0F2EB;
    --books-header: #D7DBCE;
    --books-accent: #A8AE9B;
    --books-hover: #E8ECE2;

    /* Textbooks: muted blue-grey */
    --textbooks-tab: #BCC0C5;
    --textbooks-panel: #F0F2F3;
    --textbooks-header: #D6DBDF;
    --textbooks-accent: #AAB0B6;
    --textbooks-hover: #E8ECEE;
  }

  body {
    background: var(--page-background) !important;
    background-image: none !important;
    color: var(--ink);
    font-family: "CustomFont", Georgia, serif;
  }

  .library-page {
    width: min(1400px, calc(100% - 72px));
    margin: 0 auto;
    padding: 22px 0 110px;
  }

  .library-main-title {
    margin: 0 auto 78px;

    font-family: "CustomFont", Georgia, serif;
    font-size: clamp(5rem, 9vw, 9.5rem);
    font-weight: normal;
    font-style: normal;
    line-height: 1;
    letter-spacing: 0.015em;

    color: var(--ink);
    text-align: center;
  }

  .library-section {
    position: relative;
    margin-bottom: 90px;
    padding-top: 38px;
  }

  .library-tab {
    position: absolute;
    top: 0;
    left: 38px;
    z-index: 2;

    display: flex;
    align-items: center;
    height: 54px;
    padding: 0 28px;

    border-radius: 17px 17px 0 0;
  }

  .books-section .library-tab {
    background: var(--books-tab);
  }

  .textbooks-section .library-tab {
    background: var(--textbooks-tab);
  }

  .library-tab-title {
    display: block;

    font-family: "CustomFont", Georgia, serif;
    font-size: clamp(1.7rem, 2.1vw, 2.4rem);
    font-weight: normal;
    font-style: normal;
    line-height: 1;
    letter-spacing: 0.01em;

    color: var(--ink);
    white-space: nowrap;
  }

  .library-panel {
    padding: 38px 0 0;
    border-top: 1px solid var(--line);
  }

  .books-section .library-panel {
    background: linear-gradient(
      180deg,
      rgba(184, 189, 169, 0.16) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .textbooks-section .library-panel {
    background: linear-gradient(
      180deg,
      rgba(188, 192, 197, 0.22) 0%,
      rgba(247, 244, 238, 0) 100%
    );
  }

  .table-shell {
    width: 100%;
    overflow-x: auto;
    border-radius: 18px;
    padding: 20px 22px 14px;
  }

  .books-section .table-shell {
    background: rgba(250, 251, 247, 0.94);
    border: 1px solid rgba(168, 174, 155, 0.52);
  }

  .textbooks-section .table-shell {
    background: rgba(248, 250, 251, 0.94);
    border: 1px solid rgba(170, 176, 182, 0.56);
  }

  /* DataTables controls */

  .dataTables_wrapper {
    color: var(--ink);
    font-family: var(--table-font);
    font-size: 1.08rem;
  }

  .dataTables_wrapper .dataTables_filter,
  .dataTables_wrapper .dataTables_length {
    margin-bottom: 20px;
  }

  .dataTables_wrapper .dataTables_filter input,
  .dataTables_wrapper .dataTables_length select {
    min-height: 40px;
    padding: 7px 12px !important;

    background: var(--paper-soft) !important;
    border: 1px solid var(--line-dark) !important;
    border-radius: 10px !important;

    color: var(--ink);
    font-family: var(--table-font);
    font-size: 1.02rem;
    box-shadow: none;
  }

  .books-section .dataTables_wrapper .dataTables_filter input,
  .books-section .dataTables_wrapper .dataTables_length select {
    background: #F7F9F4 !important;
    border-color: var(--books-accent) !important;
  }

  .textbooks-section .dataTables_wrapper .dataTables_filter input,
  .textbooks-section .dataTables_wrapper .dataTables_length select {
    background: #F6F8F9 !important;
    border-color: var(--textbooks-accent) !important;
  }

  /* Table */

  .table-shell table {
    width: 100% !important;
    min-width: 950px;
    border-collapse: collapse !important;
    background: transparent !important;
    color: var(--ink);
    font-family: var(--table-font);
  }

  .table-shell th,
  .table-shell td {
    padding: 16px 18px !important;
    border: none !important;
    border-bottom: 1px solid var(--line) !important;
    text-align: left;
    vertical-align: middle;
    background: transparent !important;

    font-family: var(--table-font);
    font-size: 1.04rem;
    font-weight: 400;
    line-height: 1.5;
  }

  .table-shell thead th {
    position: relative;
    padding-right: 34px !important;

    background: var(--books-header) !important;
    border-bottom: 1px solid var(--books-accent) !important;

    color: var(--ink);
    font-family: var(--table-font);
    font-size: 1.04rem;
    font-weight: 600;
    white-space: nowrap;
    cursor: pointer;
  }

  .textbooks-section .table-shell thead th {
    background: var(--textbooks-header) !important;
    border-bottom-color: var(--textbooks-accent) !important;
  }

  .table-shell thead th:first-child {
    border-radius: 10px 0 0 0;
  }

  .table-shell thead th:last-child {
    border-radius: 0 10px 0 0;
  }

  .table-shell tbody tr:last-child td {
    border-bottom: none !important;
  }

  .books-section .table-shell tbody tr:hover td {
    background: var(--books-hover) !important;
  }

  .textbooks-section .table-shell tbody tr:hover td {
    background: var(--textbooks-hover) !important;
  }

  /* Remove DataTables' blue sorting sprite */

  table.dataTable thead .sorting,
  table.dataTable thead .sorting_asc,
  table.dataTable thead .sorting_desc,
  table.dataTable thead .sorting_asc_disabled,
  table.dataTable thead .sorting_desc_disabled {
    background-image: none !important;
  }

  table.dataTable.order-column tbody tr > .sorting_1,
  table.dataTable.order-column tbody tr > .sorting_2,
  table.dataTable.order-column tbody tr > .sorting_3,
  table.dataTable.display tbody tr > .sorting_1,
  table.dataTable.display tbody tr > .sorting_2,
  table.dataTable.display tbody tr > .sorting_3 {
    background: transparent !important;
  }

  /* Subtle sorting indicators */

  table.dataTable thead th.sorting::after {
    content: "↕";
    position: absolute;
    right: 13px;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0.32;
    font-size: 0.9rem;
  }

  table.dataTable thead th.sorting_asc::after {
    content: "↑";
    position: absolute;
    right: 13px;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0.85;
    font-size: 0.95rem;
  }

  table.dataTable thead th.sorting_desc::after {
    content: "↓";
    position: absolute;
    right: 13px;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0.85;
    font-size: 0.95rem;
  }

  .books-section table.dataTable thead th.sorting_asc,
  .books-section table.dataTable thead th.sorting_desc {
    background: #CDD4C2 !important;
  }

  .textbooks-section table.dataTable thead th.sorting_asc,
  .textbooks-section table.dataTable thead th.sorting_desc {
    background: #CCD2D6 !important;
  }

  table.dataTable.no-footer {
    border-bottom: none !important;
  }

  /* Pagination */

  .dataTables_wrapper .dataTables_info {
    padding-top: 18px;
    color: rgba(48, 46, 44, 0.72);
  }

  .dataTables_wrapper .dataTables_paginate {
    padding-top: 14px;
  }

  .dataTables_wrapper .dataTables_paginate .paginate_button {
    margin-left: 3px !important;
    padding: 6px 11px !important;

    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: 8px !important;

    color: var(--ink) !important;
    font-family: var(--table-font);
    font-size: 1rem;
  }

  .books-section .dataTables_wrapper .dataTables_paginate .paginate_button:hover,
  .books-section .dataTables_wrapper .dataTables_paginate .paginate_button.current,
  .books-section .dataTables_wrapper .dataTables_paginate .paginate_button.current:hover {
    background: var(--books-header) !important;
    border-color: transparent !important;
    color: var(--ink) !important;
  }

  .textbooks-section .dataTables_wrapper .dataTables_paginate .paginate_button:hover,
  .textbooks-section .dataTables_wrapper .dataTables_paginate .paginate_button.current,
  .textbooks-section .dataTables_wrapper .dataTables_paginate .paginate_button.current:hover {
    background: var(--textbooks-header) !important;
    border-color: transparent !important;
    color: var(--ink) !important;
  }

  .dataTables_wrapper .dataTables_paginate .paginate_button.disabled,
  .dataTables_wrapper .dataTables_paginate .paginate_button.disabled:hover {
    opacity: 0.4;
    background: transparent !important;
  }

  @media (max-width: 700px) {
    .library-page {
      width: min(100% - 28px, 1400px);
      padding-top: 10px;
    }

    .library-main-title {
      margin-bottom: 55px;
      font-size: clamp(4rem, 15vw, 7rem);
    }

    .library-section {
      margin-bottom: 64px;
      padding-top: 32px;
    }

    .library-tab {
      left: 20px;
      height: 47px;
      padding: 0 19px;
      border-radius: 14px 14px 0 0;
    }

    .library-tab-title {
      font-size: clamp(1.4rem, 5vw, 1.9rem);
    }

    .library-panel {
      padding-top: 30px;
    }

    .table-shell {
      border-radius: 13px;
      padding: 14px 12px 10px;
    }

    .table-shell th,
    .table-shell td {
      padding: 13px 14px !important;
      font-size: 0.98rem;
    }

    .table-shell thead th {
      font-size: 0.98rem;
    }
  }
</style>

<div class="library-page" markdown="0">

  <h1 class="library-main-title">Library</h1>

  <section class="library-section books-section">

    <div class="library-tab">
      <span class="library-tab-title">books</span>
    </div>

    <div class="library-panel">
      <div class="table-shell">
        <div id="tableContainer1"></div>
      </div>
    </div>

  </section>

  <section class="library-section textbooks-section">

    <div class="library-tab">
      <span class="library-tab-title">textbooks</span>
    </div>

    <div class="library-panel">
      <div class="table-shell">
        <div id="tableContainer2"></div>
      </div>
    </div>

  </section>

</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it/dist/markdown-it.min.js"></script>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const md = window.markdownit();

    fetch('{{ site.baseurl }}/assets/library/readingbooks.txt')
      .then(response => {
        if (!response.ok) {
          throw new Error("Could not load readingbooks.txt");
        }

        return response.text();
      })
      .then(markdownContent => {
        document.getElementById("tableContainer1").innerHTML = md.render(markdownContent);

        const table = document.querySelector("#tableContainer1 table");

        if (table) {
          table.id = "readingbooksTable";

          $("#readingbooksTable").DataTable({
            order: [[1, "asc"]],
            pageLength: 10,
            autoWidth: false
          });
        }
      })
      .catch(error => {
        console.error(error);
        document.getElementById("tableContainer1").innerText =
          "Could not load the books table.";
      });

    fetch('{{ site.baseurl }}/assets/library/textbooks.txt')
      .then(response => {
        if (!response.ok) {
          throw new Error("Could not load textbooks.txt");
        }

        return response.text();
      })
      .then(markdownContent => {
        document.getElementById("tableContainer2").innerHTML = md.render(markdownContent);

        const table = document.querySelector("#tableContainer2 table");

        if (table) {
          table.id = "textbooksTable";

          $("#textbooksTable").DataTable({
            order: [[0, "asc"]],
            pageLength: 10,
            autoWidth: false
          });
        }
      })
      .catch(error => {
        console.error(error);
        document.getElementById("tableContainer2").innerText =
          "Could not load the textbooks table.";
      });
  });
</script>
---
title: "Library"
layout: library
excerpt: "Et Roligt Sted - Library"
sitemap: false
permalink: /library.html
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Interactive Library Tables</title>

  <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">

  <style>
    /* Page typography (keeps it consistent even if layout wraps content) */
    body {
      font-family: 'Optima', sans-serif;
    }

    /* Separate “cards” for each table */
    .content-box {
      background-color: rgba(234, 226, 226, 0.6);
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
      margin: 0 0 80px 0;
    }

    h1 {
      margin: 0 0 16px 0;
    }

    /* Table styling (avoid opacity on the entire table, it fades text too) */
    #tableContainer1 table,
    #tableContainer2 table {
      width: 100%;
      border-collapse: collapse;
      background-color: rgba(255, 255, 255, 0.75);
    }

    #tableContainer1 th, #tableContainer1 td,
    #tableContainer2 th, #tableContainer2 td {
      padding: 8px;
      border: 1px solid rgba(0, 0, 0, 0.12);
      text-align: left;
      background-color: transparent;
    }
  </style>
</head>

<body>

  <div class="content-box">
    <h1>Reading Books</h1>
    <div id="tableContainer1"></div>
  </div>

  <div class="content-box">
    <h1>Textbooks</h1>
    <div id="tableContainer2"></div>
  </div>

  <!-- Include jQuery + DataTables + markdown-it -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/markdown-it/dist/markdown-it.min.js"></script>

  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const md = window.markdownit();

      // ---------- Reading Books ----------
      fetch('{{ site.url }}{{ site.baseurl }}/_pages/readingbooks.md')
        .then(response => {
          if (!response.ok) throw new Error('Failed to load readingbooks.md');
          return response.text();
        })
        .then(markdownContent => {
          const htmlTable = md.render(markdownContent);
          document.getElementById("tableContainer1").innerHTML = htmlTable;

          const tableElement = document.querySelector("#tableContainer1 table");
          if (tableElement) {
            tableElement.id = "myTable1";
            $('#myTable1').DataTable({
              order: [[1, "asc"]] // Author surname column (index 1)
            });
          }
        })
        .catch(error => {
          console.error("Error loading or processing readingbooks.md:", error);
          document.getElementById("tableContainer1").innerText = "Error loading the reading books table.";
        });

      // ---------- Textbooks ----------
      fetch('{{ site.url }}{{ site.baseurl }}/_pages/textbooks.md')
        .then(response => {
          if (!response.ok) throw new Error('Failed to load textbooks.md');
          return response.text();
        })
        .then(markdownContent => {
          const htmlTable = md.render(markdownContent);
          document.getElementById("tableContainer2").innerHTML = htmlTable;

          const tableElement = document.querySelector("#tableContainer2 table");
          if (tableElement) {
            tableElement.id = "myTable2";
            $('#myTable2').DataTable({
              order: [[0, "desc"]] // Your current setting
            });
          }
        })
        .catch(error => {
          console.error("Error loading or processing textbooks.md:", error);
          document.getElementById("tableContainer2").innerText = "Error loading the textbooks table.";
        });
    });
  </script>

</body>
</html>

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
        table {
            width: 100%;
            border-collapse: collapse;
            opacity: 0.9; /* Semi-transparent table */
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
        }
        th, td {
            padding: 8px;
            border: 1px solid #ddd;
            text-align: left;
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background for cells */
        }
        h1 {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<h1>Reading Books</h1>
<div id="tableContainer1"></div> <!-- Container for the first table -->

<h1>Textbooks</h1>
<div id="tableContainer2"></div> <!-- Container for the second table -->

<!-- Include DataTables, jQuery, and Markdown-it -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it/dist/markdown-it.min.js"></script>

<script>
    document.addEventListener("DOMContentLoaded", () => {
        const md = window.markdownit();

        // Load and render the first table from librarytable.md
        fetch('{{ site.url }}{{ site.baseurl }}/_pages/readingbooks.md')
            .then(response => {
                if (!response.ok) throw new Error('Failed to load librarytable.md');
                return response.text();
            })
            .then(markdownContent => {
                const htmlTable = md.render(markdownContent);
                document.getElementById("tableContainer1").innerHTML = htmlTable;

                const tableElement = document.querySelector("#tableContainer1 table");
                if (tableElement) {
                    tableElement.id = "myTable1"; // Assign a unique ID to the first table
                    $('#myTable1').DataTable();
                }
            })
            .catch(error => {
                console.error("Error loading or processing librarytable.md:", error);
                document.getElementById("tableContainer1").innerText = "Error loading the library table.";
            });

        // Load and render the second table from textbooks.md
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
                    tableElement.id = "myTable2"; // Assign a unique ID to the second table
                    $('#myTable2').DataTable({
                        "order": [[1, "desc"]] // Assuming the author surname is in the second column (index 1)
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

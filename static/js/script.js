/* =====================================================
   LIBRARY BOOK ARRANGEMENT OPTIMIZER
   Main JavaScript File
   ===================================================== */


// =========================================================
// LIBRARY BOOK ARRANGEMENT OPTIMIZER
// JavaScript File
// =========================================================


// =========================================================
// PAGE LOADED
// =========================================================

// This runs when the page is completely loaded.

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "Library Book Arrangement Optimizer loaded."
        );

    }
);


// =========================================================
// BOOK SEARCH
// =========================================================

// This function searches the book table.

function searchBooks() {


    // Get the search box
    let searchInput =
        document.getElementById("bookSearch");


    // Stop if search box does not exist
    if (!searchInput) {

        return;

    }


    // Get entered text
    let searchText =
        searchInput.value.toLowerCase();


    // Get book table
    let table =
        document.getElementById("booksTable");


    // Stop if table does not exist
    if (!table) {

        return;

    }


    // Get all table rows
    let rows =
        table
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");


    // Check every row
    for (
        let i = 0;
        i < rows.length;
        i++
    ) {


        // Get row text
        let rowText =
            rows[i]
            .textContent
            .toLowerCase();


        // Show matching row
        if (
            rowText.includes(searchText)
        ) {

            rows[i].style.display = "";

        }


        // Hide non-matching row
        else {

            rows[i].style.display = "none";

        }

    }

}
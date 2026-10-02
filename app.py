# ============================================================
# LIBRARY BOOK ARRANGEMENT OPTIMIZER
# app.py
# ============================================================
# This is the main Flask file.
#
# Flask connects:
#
# HTML pages
#       ↓
# Python
#       ↓
# SQLite database
#       ↓
# Optimization Algorithm
# ============================================================

# =========================================================
# LIBRARY BOOK ARRANGEMENT OPTIMIZER
# Main Flask Application
# =========================================================

from flask import Flask, render_template, request, redirect

import sqlite3

from database import initialize_database

from optimizer import optimize_books


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# DATABASE CONNECTION
# =========================================================

def connect_db():

    # Connect to SQLite database
    conn = sqlite3.connect("library.db")

    # Return database rows like dictionaries
    conn.row_factory = sqlite3.Row

    return conn


# =========================================================
# HOME / DASHBOARD
# =========================================================

@app.route("/")
def home():

    # Connect to database
    conn = connect_db()

    cursor = conn.cursor()


    # Count total books
    cursor.execute(
        "SELECT COUNT(*) FROM books"
    )

    total_books = cursor.fetchone()[0]


    # Count total shelves
    cursor.execute(
        "SELECT COUNT(*) FROM shelves"
    )

    total_shelves = cursor.fetchone()[0]


    # Calculate average rating
    cursor.execute(
        "SELECT AVG(rating) FROM books"
    )

    average_rating = cursor.fetchone()[0]


    # If there are no books
    # average rating will be None
    if average_rating is None:

        average_rating = 0

    else:

        average_rating = round(
            average_rating,
            1
        )


    # Count different categories
    cursor.execute("""
        SELECT COUNT(DISTINCT category)
        FROM books
    """)

    total_categories = cursor.fetchone()[0]


    # Close database
    conn.close()


    # Send information to dashboard
    return render_template(
        "index.html",
        total_books=total_books,
        total_shelves=total_shelves,
        average_rating=average_rating,
        total_categories=total_categories
    )


# =========================================================
# BOOKS PAGE
# =========================================================

@app.route("/books")
def books():

    # Connect database
    conn = connect_db()

    cursor = conn.cursor()


    # Get all books
    cursor.execute("""
        SELECT *
        FROM books
        ORDER BY id
    """)

    books = cursor.fetchall()


    # Close database
    conn.close()


    # Send books to HTML page
    return render_template(
        "books.html",
        books=books
    )


# =========================================================
# ADD BOOK
# =========================================================

@app.route("/add_book", methods=["POST"])
def add_book():

    # Get book name from form
    name = request.form["name"].strip()


    # Get category from form
    category = request.form["category"].strip()


    # Get rating from form
    rating = float(request.form["rating"])


    # Check that name is not empty
    if not name:

        return "Book name is required"


    # Check that category is not empty
    if not category:

        return "Category is required"


    # Check rating
    if rating < 0 or rating > 10:

        return "Rating must be between 0 and 10"


    # Connect database
    conn = connect_db()

    cursor = conn.cursor()


    # Insert book into database
    cursor.execute("""
        INSERT INTO books
        (name, category, rating, current_shelf)

        VALUES (?, ?, ?, ?)
    """, (
        name,
        category,
        rating,
        None
    ))


    # Save changes
    conn.commit()


    # Close database
    conn.close()


    # Return to Books page
    return redirect("/books")


# =========================================================
# SHELVES PAGE
# =========================================================

@app.route("/shelves")
def shelves():

    # Connect database
    conn = connect_db()

    cursor = conn.cursor()


    # Get shelves
    cursor.execute("""
        SELECT *
        FROM shelves
        ORDER BY search_time
    """)

    shelves_data = cursor.fetchall()


    # Create a list for final shelf information
    shelves = []


    # Calculate book count for every shelf
    for shelf in shelves_data:


        cursor.execute("""
            SELECT COUNT(*)
            FROM books
            WHERE current_shelf = ?
        """, (shelf["name"],))


        book_count = cursor.fetchone()[0]


        # Add shelf information
        shelves.append({

            "id": shelf["id"],

            "name": shelf["name"],

            "capacity": shelf["capacity"],

            "search_time": shelf["search_time"],

            "book_count": book_count

        })


    # Close database
    conn.close()


    # Send shelf information to page
    return render_template(
        "shelves.html",
        shelves=shelves
    )


# =========================================================
# OPTIMIZATION
# =========================================================

@app.route("/optimize")
def optimize():

    # Connect database
    conn = connect_db()

    cursor = conn.cursor()


    # Get all books
    cursor.execute("""
        SELECT *
        FROM books
    """)

    books_data = cursor.fetchall()


    # Get all shelves
    cursor.execute("""
        SELECT *
        FROM shelves
        ORDER BY search_time
    """)

    shelves_data = cursor.fetchall()


    # Run Greedy Algorithm
    results = optimize_books(
        books_data,
        shelves_data
    )


    # -----------------------------------------------------
    # Update allocated shelf in database
    # -----------------------------------------------------

    for result in results:

        cursor.execute("""
            UPDATE books

            SET current_shelf = ?

            WHERE id = ?
        """, (
            result["shelf"],
            result["id"]
        ))


    # Save shelf allocations
    conn.commit()


    # Calculate total search cost
    total_cost = sum(
        result["search_cost"]
        for result in results
    )


    # Close database
    conn.close()


    # Show optimization results
    return render_template(
        "results.html",
        results=results,
        total_cost=round(total_cost, 2)
    )


# =========================================================
# RESULTS PAGE
# =========================================================

@app.route("/results")
def results_page():

    # Connect database
    conn = connect_db()

    cursor = conn.cursor()


    # Get allocated books
    cursor.execute("""
        SELECT
            books.id,
            books.name,
            books.rating,
            books.current_shelf,
            shelves.search_time

        FROM books

        LEFT JOIN shelves
        ON books.current_shelf = shelves.name

        WHERE books.current_shelf IS NOT NULL

        ORDER BY books.rating DESC
    """)


    allocated_books = cursor.fetchall()


    # Create result list
    results = []


    # Calculate search cost
    for book in allocated_books:


        search_time = book["search_time"]


        search_cost = (
            book["rating"] * search_time
        )


        results.append({

            "id": book["id"],

            "book": book["name"],

            "rating": book["rating"],

            "shelf": book["current_shelf"],

            "search_time": search_time,

            "search_cost": round(
                search_cost,
                2
            )

        })


    # Calculate total cost
    total_cost = sum(
        result["search_cost"]
        for result in results
    )


    # Close database
    conn.close()


    # Display results
    return render_template(
        "results.html",
        results=results,
        total_cost=round(
            total_cost,
            2
        )
    )


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":
    initialize_database()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
    
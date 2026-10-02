# ============================================================
# optimizer.py
# ============================================================
# This file contains the Greedy Algorithm.
#
# Basic idea:
#
# 1. Highly rated books get higher priority.
# 2. Faster shelves are used first.
# 3. Shelf capacity is respected.
#
# This is the main DAA part of our project.
# ============================================================


# =========================================================
# LIBRARY BOOK ARRANGEMENT OPTIMIZER
# Greedy Algorithm
# =========================================================


# =========================================================
# OPTIMIZE BOOKS
# =========================================================

def optimize_books(books, shelves):

    # -----------------------------------------------------
    # Step 1: Sort books by rating
    # Highest rated book comes first
    # -----------------------------------------------------

    sorted_books = sorted(
        books,
        key=lambda book: book["rating"],
        reverse=True
    )


    # -----------------------------------------------------
    # Step 2: Sort shelves by search time
    # Fastest shelf comes first
    # -----------------------------------------------------

    sorted_shelves = sorted(
        shelves,
        key=lambda shelf: shelf["search_time"]
    )


    # This list stores final results
    results = []


    # Current shelf position
    shelf_index = 0


    # Number of books already placed
    # on the current shelf
    books_in_shelf = 0


    # -----------------------------------------------------
    # Step 3: Allocate every book
    # -----------------------------------------------------

    for book in sorted_books:


        # Check whether shelves are available
        if shelf_index >= len(sorted_shelves):

            # No more shelf space
            break


        # Get current shelf
        shelf = sorted_shelves[shelf_index]


        # -------------------------------------------------
        # Step 4: Check shelf capacity
        # -------------------------------------------------

        if books_in_shelf >= shelf["capacity"]:

            # Move to the next shelf
            shelf_index += 1

            # Reset book count
            books_in_shelf = 0


            # Check again for available shelf
            if shelf_index >= len(sorted_shelves):

                break


            # Get new shelf
            shelf = sorted_shelves[shelf_index]


        # -------------------------------------------------
        # Step 5: Calculate search cost
        # -------------------------------------------------

        search_cost = (
            book["rating"] * shelf["search_time"]
        )


        # -------------------------------------------------
        # Step 6: Store allocation result
        # -------------------------------------------------

        results.append({

            "id": book["id"],

            "book": book["name"],

            "rating": book["rating"],

            "shelf": shelf["name"],

            "search_time": shelf["search_time"],

            "search_cost": round(search_cost, 2)

        })


        # Increase number of books in shelf
        books_in_shelf += 1


    # Return final arrangement
    return results
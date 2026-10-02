# =========================================================
# LIBRARY BOOK ARRANGEMENT OPTIMIZER
# Database File
# =========================================================

import sqlite3


# Name of our SQLite database
DATABASE = "library.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def connect_db():

    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)

    # Allows us to access columns using column names
    conn.row_factory = sqlite3.Row

    return conn


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

def create_tables():

    # Open database connection
    conn = connect_db()

    cursor = conn.cursor()


    # -----------------------------------------------------
    # Create Books table
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            category TEXT NOT NULL,

            rating REAL NOT NULL,

            current_shelf TEXT

        )
    """)


    # -----------------------------------------------------
    # Create Shelves table
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shelves (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            capacity INTEGER NOT NULL,

            search_time REAL NOT NULL

        )
    """)


    # Save database changes
    conn.commit()

    # Close connection
    conn.close()


# =========================================================
# ADD DEFAULT SHELVES
# =========================================================

def add_default_shelves():

    conn = connect_db()

    cursor = conn.cursor()


    # Check whether shelves already exist
    cursor.execute("SELECT COUNT(*) FROM shelves")

    count = cursor.fetchone()[0]


    # Add shelves only if the table is empty
    if count == 0:

        shelves = [

            ("Shelf 1", 20, 1.0),
            ("Shelf 2", 20, 2.0),
            ("Shelf 3", 20, 3.0),
            ("Shelf 4", 20, 4.0),
            ("Shelf 5", 20, 5.0)

        ]


        # Insert all default shelves
        cursor.executemany("""
            INSERT INTO shelves
            (name, capacity, search_time)
            VALUES (?, ?, ?)
        """, shelves)


    conn.commit()

    conn.close()


# =========================================================
# INITIALIZE DATABASE
# =========================================================

def initialize_database():

    # Create tables
    create_tables()

    # Add default shelves
    add_default_shelves()


# =========================================================
# RUN THIS FILE DIRECTLY
# =========================================================

if __name__ == "__main__":

    initialize_database()

    print("Database created successfully!")
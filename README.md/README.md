# 📚 Library Book Arrangement Optimizer

## 1. Project Overview

The Library Book Arrangement Optimizer is a smart library management system
that helps arrange books on shelves efficiently.

The system uses a Greedy Algorithm to assign highly rated books to shelves
with lower search time while considering the capacity of each shelf.

The main objective is to reduce the time required to find important books
in a library.

The project combines:

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Greedy Algorithm


## 2. Problem Statement

In a large library, many books are stored on different shelves.

If books are not arranged properly, users may spend more time searching
for important or highly rated books.

Manual arrangement can also become difficult when:

- The number of books increases
- Shelf capacities are different
- Shelves have different search times
- Books have different ratings

Therefore, an automated system is required to arrange books efficiently.


## 3. Proposed Solution

The proposed system is a Library Book Arrangement Optimizer.

The system:

1. Stores book information.
2. Stores shelf information.
3. Takes the rating of each book.
4. Checks shelf capacity.
5. Checks shelf search time.
6. Sorts books according to rating.
7. Sorts shelves according to search time.
8. Assigns highly rated books to faster shelves.
9. Calculates the search cost.
10. Displays the optimized arrangement.


## 4. Main Objective

The main objectives of this project are:

- To manage library books digitally.
- To manage different shelves.
- To arrange books efficiently.
- To reduce book searching time.
- To apply the Greedy Algorithm in a real-world problem.
- To provide a simple and user-friendly interface.
- To show optimization results clearly.


## 5. Algorithm Used

### Greedy Algorithm

This project uses the Greedy Algorithm.

A Greedy Algorithm makes the best available choice at each step.

In this project:

- Books are sorted from highest rating to lowest rating.
- Shelves are sorted from lowest search time to highest search time.
- Highly rated books are assigned to faster shelves.
- Shelf capacity is checked before assigning books.

This provides a simple and efficient arrangement strategy.


## 6. Book Rating

Each book has a rating.

For example:

| Book | Rating |
|------|--------|
| Mahabharata | 9.8 |
| Python Programming | 9.5 |
| DBMS | 9.0 |
| Data Structures | 8.8 |

A higher rating means the book receives higher priority
during the arrangement process.


## 7. Shelf Information

Each shelf contains:

- Shelf Name
- Capacity
- Search Time

Example:

| Shelf | Capacity | Search Time |
|------|----------|-------------|
| Shelf A | 10 books | 1 minute |
| Shelf B | 15 books | 2 minutes |
| Shelf C | 20 books | 3 minutes |

Shelves with lower search time are considered faster shelves
for the optimization process.


## 8. Search Cost

The project uses the following formula:

Search Cost = Rating × Search Time

For example:

Book Rating = 9.5

Search Time = 2 minutes

Search Cost:

9.5 × 2 = 19


The system calculates the search cost for every allocated book.

The total search cost is:

Total Search Cost = Sum of all Book Search Costs


## 9. How the Optimization Works

The optimization process follows these steps.

### Step 1: Get Books

The system gets all books from the SQLite database.

### Step 2: Get Shelves

The system gets all shelves from the database.

### Step 3: Sort Books

Books are sorted according to rating.

Highest-rated books are considered first.

### Step 4: Sort Shelves

Shelves are sorted according to search time.

The shelf with the lowest search time is considered first.

### Step 5: Check Capacity

Before assigning a book, the system checks whether the shelf
has available space.

### Step 6: Allocate Books

The system assigns books to shelves.

Highly rated books are assigned to faster shelves.

### Step 7: Calculate Search Cost

The system calculates:

Rating × Search Time

for every book.

### Step 8: Display Results

The final arrangement is displayed on the Optimization Results page.


## 10. Technologies Used

### Python

Python is used for the backend and algorithm implementation.

### Flask

Flask is a Python web framework.

It connects the frontend with the backend.

### SQLite

SQLite is used to store:

- Book information
- Shelf information
- Ratings
- Shelf allocation


### HTML

HTML is used to create the structure of the web pages.

### CSS

CSS is used to design the website.

It controls:

- Colors
- Layout
- Cards
- Tables
- Buttons
- Responsive design


### JavaScript

JavaScript is used to add interactive features.

For example:

- Book searching
- User interaction
- Browser-side functions


## 11. Database

The project uses SQLite.

The database file is:

library.db

The main tables are:

### Books Table

The books table stores book information such as:

- ID
- Book name
- Category
- Rating
- Current shelf


### Shelves Table

The shelves table stores:

- ID
- Shelf name
- Capacity
- Search time


## 12. Website Pages

The project contains the following pages.

### Dashboard

The Dashboard provides an overview of the library.

It can display:

- Total number of books
- Total number of shelves
- Average rating
- Number of categories
- Project information


### Books Page

The Books page displays all books.

It shows:

- Book ID
- Book name
- Category
- Rating
- Allocated shelf

A search box is also provided to find books quickly.


### Shelves Page

The Shelves page displays shelf information.

It shows:

- Shelf name
- Capacity
- Search time
- Number of allocated books
- Shelf availability


### Optimization Page

The Optimization page starts the Greedy Algorithm.

It arranges books according to rating and shelf search time.


### Results Page

The Results page displays:

- Book name
- Rating
- Allocated shelf
- Search time
- Search cost
- Total search cost


## 13. Project Structure

```text
LibraryBookOptimizer
│
├── app.py
├── optimizer.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── shelves.html
│   └── results.html
│
└── static
    ├── css
    │   └── style.css
    │
    ├── js
    │   └── script.js
    │
    └── images
        └── logo.png


LIBRARY BOOK ARRANGEMENT OPTIMIZER - PROFESSIONAL DEMO

1. Put this folder in your preferred location.
2. Open the folder in VS Code.
3. Make sure logo.png is here:
   static/images/logo.png
4. Open a terminal in this folder.
5. Run:
      pip install -r requirements.txt
6. Run:
      python database.py
7. Start the website:
      python app.py
8. Open:
      http://127.0.0.1:5000

IMPORTANT IF YOUR OLD library.db HAS 500 DUPLICATE BOOKS:
- Stop Flask with Ctrl+C.
- Delete the old library.db once.
- Run: python database.py
- Then run: python app.py

The new database will contain 100 demo books and 5 shelves.

PROJECT POINTS:
1. Problem Understanding - reduce book search time.
2. Innovation - rating-based smart shelf priority.
3. Technical Implementation - Flask + SQLite + Greedy Algorithm.
4. Functionality - search, category filter, shelf allocation, optimization.
5. Practical Impact - faster access to highly rated/popular books.
6. UI/UX - responsive dashboard, cards, table, badges and your logo.
7. Presentation - explain the workflow: Database -> Sorting -> Greedy Assignment -> Result.
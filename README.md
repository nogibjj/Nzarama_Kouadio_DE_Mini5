## Mini Project 5: SQLite Lab
INCLUDE BADGE 

# Student Database CRUD Operations

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations on a **students** table using a SQLite database in Python. The project includes a simple Python script for performing these operations and a test file to validate the functionality.

# Project Overview

The main script (`db_operations.py`) connects to an SQLite database and performs the following operations:
- **Create**: Insert a new student record.
- **Read**: Retrieve all student records.
- **Update**: Modify the grade of a student.
- **Delete**: Remove a student record.

The tests for these CRUD operations are provided in `main_test.py` and can be run using `pytest`.

# Important Folders in our

.
├── main.py                 # Main Python script for CRUD operations
├── README.md               # Project documentation
├── requirements.txt        # Dependencies (pytest for testing)
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD pipeline
└── main_test.py            # Test file for CRUD operations using pytest

# Table Structure

The **students** table has the following columns:
- `id`: Unique identifier for each student (auto-incremented).
- `name`: Name of the student (text).
- `age`: Age of the student (integer).
- `grade`: Grade of the student (text).

# Setup Instructions

- Clone the repository: git clone
- Install dependencies: pip install -r requirements.txt
- Run main.py




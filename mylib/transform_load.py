import sqlite3
import csv
import os


# Load the CSV file and insert data into a new SQLite3 database
def load(file_path):
    """
    Transforms and Loads data into the local SQLite3 database.
    Example:
    Columns: id (primary key), year, month, date_of_month, day_of_week, births
    """

    # Print the full working directory and path
    print(os.getcwd())

    # Open the CSV file
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")

        # Connect to the SQLite database (it will create a new one if it doesn't exist)
        conn = sqlite3.connect("BirthsDB.db")
        c = conn.cursor()

        # Drop the table if it exists, and create a new one with an auto-incrementing primary key
        c.execute("DROP TABLE IF EXISTS births")
        c.execute(
            """
        CREATE TABLE births (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            month INTEGER,
            date_of_month INTEGER,
            day_of_week INTEGER,
            births INTEGER
        )
        """
        )

        # Insert the CSV data into the table, skipping the header row
        next(payload)  # Skip header row
        c.executemany(
            """
        INSERT INTO births (year, month, date_of_month, day_of_week, births)
        VALUES (?, ?, ?, ?, ?)
        """,
            payload,
        )

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    print(f"Data from {file_path} has been successfully loaded into the database.")
    return "BirthsDB.db"

import sqlite3


# Modify query_data to accept a query string
def query_data(query_string):
    """
    Run a custom query passed as an argument
    """
    # Connect to the BirthsDB database
    conn = sqlite3.connect("BirthsDB.db")
    cursor = conn.cursor()

    # Execute the provided query string
    cursor.execute(query_string)

    # Fetch and print the results
    rows = cursor.fetchall()
    print("Query results:")
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

    return "Query Success"


# DOING ALL CRUD OPERATIONS BELOW


# Create function to add a new record
def create_birth_record(year, month, day_of_month, day_of_week, births):
    conn = sqlite3.connect("BirthsDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    INSERT INTO births (year, month, date_of_month, day_of_week, births)
    VALUES (?, ?, ?, ?, ?)
    """,
        (year, month, day_of_month, day_of_week, births),
    )
    conn.commit()
    conn.close()


# Update function
def update_birth_record(id, new_birth_count):
    conn = sqlite3.connect("BirthsDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    UPDATE births
    SET births = ?
    WHERE id = ?
    """,
        (new_birth_count, id),
    )
    conn.commit()
    conn.close()


# Delete function
def delete_birth_record(id):
    conn = sqlite3.connect("BirthsDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    DELETE FROM births
    WHERE id = ?
    """,
        (id,),
    )
    conn.commit()
    conn.close()


# Read function (fetch top 5 rows)
def read_top_records():
    conn = sqlite3.connect("BirthsDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM births LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    return rows

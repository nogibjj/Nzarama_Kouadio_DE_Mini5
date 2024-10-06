import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a students table if it doesn't exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
"""
)
conn.commit()


# Insert a new student
def insert_student(name, age, grade):
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade)
    )
    conn.commit()


# Retrieve all students
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


# Update a student's grade
def update_student_grade(name, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    conn.commit()


# Delete a student by name
def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()


# Testing the basic operations
if __name__ == "__main__":
    # Insert some students
    insert_student("Alice", 20, "A")
    insert_student("Bob", 22, "B")

    # Read and print all students
    students = get_students()
    print("Students:", students)

    # Update Bob's grade
    update_student_grade("Bob", "A+")
    print("After updating Bob's grade:", get_students())

    # Delete Alice
    delete_student("Alice")
    print("After deleting Alice:", get_students())

    # Close the database connection
    conn.close()

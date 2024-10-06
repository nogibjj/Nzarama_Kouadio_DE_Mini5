import sqlite3
import pytest


# Set up an in-memory database for testing
@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")  # Use in-memory database for testing
    cursor = connection.cursor()
    cursor.execute(
        """
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """
    )
    connection.commit()
    yield connection
    connection.close()


# Test inserting a student
def test_insert_student(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        ("Test Student", 20, "A"),
    )
    conn.commit()
    cursor.execute("SELECT * FROM students WHERE name = ?", ("Test Student",))
    result = cursor.fetchone()
    assert result is not None
    assert result[1] == "Test Student"


# Test retrieving students
def test_get_students(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        ("Test Student", 20, "A"),
    )
    conn.commit()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    assert len(result) == 1


# Test updating a student's grade
def test_update_student_grade(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        ("Test Student", 20, "B"),
    )
    conn.commit()
    cursor.execute(
        "UPDATE students SET grade = ? WHERE name = ?", ("A+", "Test Student")
    )
    conn.commit()
    cursor.execute("SELECT grade FROM students WHERE name = ?", ("Test Student",))
    result = cursor.fetchone()
    assert result[0] == "A+"


# Test deleting a student
def test_delete_student(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        ("Test Student", 20, "A"),
    )
    conn.commit()
    cursor.execute("DELETE FROM students WHERE name = ?", ("Test Student",))
    conn.commit()
    cursor.execute("SELECT * FROM students WHERE name = ?", ("Test Student",))
    result = cursor.fetchone()
    assert result is None

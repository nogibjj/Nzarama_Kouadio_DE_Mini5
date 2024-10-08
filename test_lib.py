from mylib.query import query_data
from mylib.extract import extract
from mylib.transform_load import load


def test_query():
    # Testing query function
    result = query_data("SELECT * FROM births LIMIT 5")
    assert isinstance(result, str), "Query did not return a string"
    print("Query test passed.")


def test_extract():
    # Testing extract function to check if the CSV file is downloaded correctly
    file_path = extract()
    assert file_path.endswith(".csv"), "Extract did not return a valid CSV file"
    print("Extract function test passed.")


def test_transform_load():
    # Testing load function to check if the data is loaded into SQLite
    file_path = extract()
    db_file = load(file_path)
    assert db_file.endswith(".db"), "Load did not create a readable DB file"
    print("Transform and load test passed.")


if __name__ == "__main__":
    test_query()
    test_extract()
    test_transform_load()

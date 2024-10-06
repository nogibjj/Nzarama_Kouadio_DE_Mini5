import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_data


def main(query_string=None):
    # Step 1: Extract the data
    print("Extracting data...")
    file_path = extract()

    # Step 2: Transform and load the data into the SQLite database
    print("Transforming data...")
    load(file_path)

    # Step 3: Run custom query if given
    if query_string:
        print("Running custom query...")
        query_data(query_string)
    else:
        print("No custom query provided. Defaulting to a SELECT * query.")
        query_data("SELECT * FROM births LIMIT 5")


if __name__ == "__main__":
    fire.Fire(main)

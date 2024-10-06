"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

US Birth dataset
"""

import requests


def extract():
    url = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/births/US_births_2000-2014_SSA.csv"
    file_path = "dataset/US_births_2000-2014_SSA.csv"

    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    # Print confirmation message to show the file was downloaded successfully
    print(f"File downloaded successfully and saved to {file_path}")

    return file_path

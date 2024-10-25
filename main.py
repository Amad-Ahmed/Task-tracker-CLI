import json
import os
import argparse


# function to make json if not present or load json with name
def load_json(file_name):
    # check if json already exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
            print(f"Data Loaded from {file_name}")
    else:
        with open(file_name, "w") as file:
            default_data = {}
            json.dump(default_data, file, indent=4)
            data = default_data
            print(f"Json file {file_name} created with Default Data")
    return data


# load and create json
json_path = "data.json"
data = load_json(json_path)

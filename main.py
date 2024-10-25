import json
import os
import argparse
from datetime import datetime


# Function to load JSON if it exists or create it if not
def load_json(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
            print(f"Data loaded from {file_name}")
    else:
        data = []
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
            print(f"JSON file {file_name} created with default data")
    return data


# Function to get the next ID by finding the max ID in current data
def get_next_id(data):
    if not data:
        return 1  # Start at 1 if there are no tasks
    max_id = max(task["id"] for task in data)
    return max_id + 1


# Function to add a task to JSON
def add_task(file_name, data, task):
    task_id = get_next_id(data)
    task_body = {
        "id": task_id,
        "description": task,
        "status": "todo",
        "createdAt": datetime.now().timestamp(),
        "updatedAt": "",
    }
    data.append(task_body)
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Task added with ID {task_id}")


# Load or create JSON
json_path = "data.json"
data = load_json(json_path)

# CLI argument handling
parser = argparse.ArgumentParser(description="Task CLI - Manage your tasks.")
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", type=str, help="Description of the task.")

# Parse arguments
args = parser.parse_args()

# Execute based on subcommand
if args.command == "add":
    add_task(json_path, data, args.description)

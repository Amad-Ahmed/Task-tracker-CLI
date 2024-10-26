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


# Function to delete a task from JSON
def delete_task(file_name, data, id):
    # find and delete the task by searching on basis of id
    updated_data = [task for task in data if task["id"] != id]

    # prompt if no task was found
    if len(updated_data) == len(data):
        print(f"No task with ID :: {id} was found.")
    else:
        with open(file_name, "w") as file:
            json.dump(updated_data, file, indent=4)
        print(f"Task with ID :: {id} was deleted.")


# Function to update a task in JSON
def update_task(file_name, data, id, task):
    # find the task in json and update description
    updated_data = [task for task in data if task["id"] != id]
    if len(updated_data) == len(data):
        print(f"No task found with ID :: {id}")
    else:
        task_tochange = [task for task in data if task["id"] == id]
        task_tochange[0]["description"] = task
        updated_data.append(task_tochange[0])

        with open(file_name, "w") as file:
            json.dump(updated_data, file, indent=4)
        print(f"Task updated with ID {id}")


# Load or create JSON
json_path = "data.json"
data = load_json(json_path)

# CLI argument handling
parser = argparse.ArgumentParser(description="Task CLI - Manage your tasks.")
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", type=str, help="Description of the task.")

# Delete subcommand
delete_parser = subparsers.add_parser("delete", help="Delete a task based on id")
delete_parser.add_argument("ID", type=int, help="ID of the task to delete.")

# Update subcommand
update_parser = subparsers.add_parser(
    "update", help="Update an existing task on basis of id."
)
update_parser.add_argument("ID", type=int, help="ID of the task to update.")
update_parser.add_argument(
    "description", type=str, help="Updated description of the task to be updated."
)

# Parse arguments
args = parser.parse_args()

# Execute based on subcommand
if args.command == "add":
    add_task(json_path, data, args.description)
elif args.command == "delete":
    delete_task(json_path, data, args.ID)
elif args.command == "update":
    update_task(json_path, data, args.ID, args.description)

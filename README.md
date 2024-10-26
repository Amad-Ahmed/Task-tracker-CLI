# Task CLI Manager

This project is a command-line interface (CLI) application for managing tasks. It allows you to create, update, delete, list, and change the status of tasks in a JSON file. Each task has an ID, description, status, and timestamps to indicate when it was created and last updated.

## Features

- Add tasks with descriptions
- Delete tasks by ID
- Update task descriptions by ID
- Mark tasks as "in-progress" or "done"
- List tasks filtered by their status (`todo`, `in-progress`, `done`)
- All tasks are stored in a `data.json` file in the root directory.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. (Optional) Set up a virtual environment and install dependencies if needed:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

Run the `main.py` file with one of the following commands to manage tasks:

### Commands

#### Add a Task

To add a new task with a description:

```bash
python main.py add "Description of the task"
```

#### Delete a Task

To delete a task by its ID:

```bash
python main.py delete <task_id>
```

#### Update a Task

To update the description of a task by its ID:

```bash
python main.py update <task_id> "New description of the task"
```

#### Mark a Task as In-Progress

To mark a task as "in-progress" by its ID:

```bash
python main.py mark-in-progress <task_id>
```

#### Mark a Task as Done

To mark a task as "done" by its ID:

```bash
python main.py mark-done <task_id>
```

#### List Tasks

To list all tasks or filter them by status:

```bash
python main.py list [status]
```

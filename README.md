# Python Task Manager

## About the Project

**Python Task Manager** is a command-line application for managing a list of tasks.

Users can:

* add new tasks,
* display existing tasks,
* mark tasks as completed,
* delete tasks,
* save and load tasks using a JSON file.

The main goal of the project was to gain practical experience with **Object-Oriented Programming (OOP)** in Python, modular application design, JSON data persistence, and unit testing with `pytest`.

## Features

* Task creation and deletion
* Task completion
* Task list display
* JSON data persistence
* Input validation
* Unit tests with `pytest`

## Technologies

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON**
* **pytest**
* **Git / GitHub**

## Project Structure

| File              | Responsibility                                     |
| ----------------- | -------------------------------------------------- |
| `main.py`         | Application menu and user interaction              |
| `task.py`         | `Task` class representing a single task            |
| `task_manager.py` | `TaskManager` class responsible for managing tasks |
| `storage.py`      | Reading and writing task data to JSON              |
| `tasks.json`      | Persistent application data                        |
| `tests/`          | Unit tests                                         |

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd python-task-manager
```

### Run the Application

```bash
python main.py
```

The application will start in the terminal and display the task management menu.

## Running Tests

The project uses **pytest** for unit testing.

Run the complete test suite with:

```bash
python -m pytest
```

The test suite covers:

* adding tasks,
* finding tasks,
* completing tasks,
* deleting tasks,
* handling invalid task IDs.

All current tests pass successfully.

## Example

```text
=== TASK MANAGER ===

1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

Example task list:

```text
1. [ ] Go to the gym
2. [x] Buy groceries
3. [ ] Study Python
```

## Future Improvements

Possible future improvements include:

* task priorities,
* due dates,
* filtering and sorting,
* additional unit tests.

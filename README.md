#  Task Tracker (Command-Line Application)

A modular and efficient **Command-Line Task Management System** built in Python.
This application enables users to manage daily tasks with structured workflows, persistent storage, and clean code practices following modern Python development standards.

---

##  Overview

The Task Tracker is designed to simplify task management directly from the terminal.
It supports full CRUD operations, task status tracking, and modular architecture, making it both user-friendly and developer-friendly.

---

##  Key Features

* **Task Management**

  * Add new tasks
  * Update existing tasks
  * Delete tasks

* **Status Tracking**

  * Not Started
  * In Progress
  * Completed

* **Task Filtering**

  * View all tasks
  * Filter tasks by status

* **Persistent Storage**

  * Data stored in JSON format for simplicity and portability

* **Modular Code Architecture**

  * Separation of concerns for scalability and maintainability

---

##  Project Structure

```id="nq6ot6"
task-tracker/
│
├── src/
│   └── task_tracker/
│       ├── main.py          # Entry point
│       ├── storage.py       # File handling (JSON)
│       ├── task_manager.py  # Core task operations
│       └── display.py       # Output & display logic
│
├── tasks.json               # Data storage
├── pyproject.toml           # Project configuration
├── uv.lock                  # Dependency lock file
├── README.md
└── .venv
```

---

##  Technology Stack

* **Python** (Core language)
* **uv** (Modern package & environment manager)
* **Ruff** (Linting and code quality)
* **Black** (Code formatting)

---

##  Setup & Installation

### 1. Clone the repository

```id="d35v1f"
git clone https://github.com/Mr-chandresh/task-tracker.git
cd task-tracker
```

### 2. Create virtual environment

```id="7p1k1u"
uv venv
```

### 3. Activate environment (Windows)

```id="6wgqmh"
.venv\Scripts\activate
```

### 4. Install dependencies

```id="yy8bdr"
uv sync
```

---

##  Usage

Run the application:

```id="9lzh6g"
uv run python src/task_tracker/main.py
```

Follow the interactive menu to perform task operations.

---

##  Architecture

The project follows a modular design:

* **storage.py** → Handles file operations (load/save tasks)
* **task_manager.py** → Contains business logic for task operations
* **display.py** → Manages user-facing output
* **main.py** → Entry point and control flow

This separation improves readability, maintainability, and scalability.

---

##  Code Quality & Formatting

### Linting (Ruff)

```id="d3v2cj"
uv run ruff check .
uv run ruff check . --fix
```

### Formatting (Black)

```id="vrnuxl"
uv run black .
```

---

##  Development Workflow

```id="uyk3oj"
uv run ruff check . --fix
uv run black .
uv run ruff check .
```

---

##  Future Enhancements

* Task search functionality
* Priority levels and due dates
* Rich CLI interface (colored output)
* Conversion to GUI/Desktop application
* Web-based task management system

---

##  Author

**Chandresh Sharma**

---

##  Note

This project demonstrates practical implementation of:

* Clean code principles
* Modular architecture
* Modern Python tooling
* CLI-based application design



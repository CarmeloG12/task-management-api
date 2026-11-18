# Task Management REST API

A backend task management application built with Python, FastAPI, SQLite, and Pydantic. This project is designed to practice REST API development, database integration, and data validation.

**Project Status:** In Progress

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Features

- Create new tasks
- Retrieve all tasks
- Update existing tasks
- Delete tasks
- Validate incoming data using Pydantic
- Store task information in an SQLite database
- Handle errors when requested tasks cannot be found

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/tasks` | Retrieve all tasks |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CarmeloG12/task-management-api.git
```

2. Navigate into the project:

```bash
cd task-management-api
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Example Request

Create a task using POST `/tasks`:

```json
{
  "title": "Learn FastAPI"
}
```

Task titles must contain between 3 and 100 characters.

## Learning Goals

- Understand REST API architecture
- Practice CRUD operations
- Work with relational databases
- Implement data validation
- Handle HTTP errors
- Improve Python backend development skills

## Developer

**Carmelo Gonzalez**

Information Technology Student  
University of Cincinnati

GitHub: https://github.com/CarmeloG12

---

This project is actively being developed as part of my journey toward becoming a software engineer.
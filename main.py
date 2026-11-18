#FastAPI application for task management with SQLite database integration.
from fastapi import FastAPI, HTTPException
from database import get_connection, create_table
from pydantic import BaseModel, Field

app = FastAPI()

class Task(BaseModel): #Creates pydantic model 
    title: str = Field(min_length=3, max_length=100)

create_table()


@app.get("/")
def home():
    return {"message": "Task Management API is running!"}


@app.get("/tasks")
def get_tasks():
    connection = get_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()

    connection.close()

    return {"tasks": [dict(task) for task in tasks]}


@app.post("/tasks")
def create_task(task: Task):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (task.title,)
    )

    connection.commit()

    new_task_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Task created successfully",
        "id": new_task_id,
        "title": task.title
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET title = ? WHERE id = ?",
        (updated_task.title, task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Task not found")

    connection.close()

    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Task not found")

    connection.close()

    return {"message": "Task deleted successfully"}

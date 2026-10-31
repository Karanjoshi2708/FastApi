from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool


@app.post("/todo")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "msg":"todo created",
        "data":todo
    }


@app.get("/todo")
def get_todos():
    return todos


@app.get("/todo/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {
        "error ":"todo not found"
    }

@app.put("/todo/{todo_id}")
def update_todo(todo_id:int, updates_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updates_todo
            return {
                "msg":"todo updated",
                "data":updates_todo
            }
    return {
        "error ":"todo not found"
    }


@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "msg":"data deleted"
            }
    return {
        "error ":"todo not found"
    }
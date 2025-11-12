from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo API")

class Todo(BaseModel):
    id: int
    title: str
    done: bool = False

todos: list[Todo] = []

@app.get("/todos")
def get_all():
    return todos

@app.post("/todos")
def create(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="Duplicate id")
    todos.append(todo)
    return todo

@app.patch("/todos/{todo_id}")
def toggle(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            t.done = not t.done
            return t
    raise HTTPException(status_code=404, detail="Not found")

from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
async def view_todos():
    return todos

@app.post("/create")
async def create_todo(todo):
    todos.append(todo)
    return todos

@app.get("/delete/{todo_id}")
async def delete_todo(todo_id: int):
    if todo_id  < len(todos):
        return {"Todo deleted" : todos.pop(todo_id),
                "To-Do List" : todos}
    else:
        return {"Error": "No todo found with that ID",
                "To-Do List" : todos}
    
@app.post("/update/{todo_id}")
async def update_todo(todo_id: int, newtodo: str):
    if todo_id < len(todos):
        todos[todo_id] = newtodo
        return newtodo
    else:
        return {"Error": "No todo found with that ID",
                "To-Do List" : todos}
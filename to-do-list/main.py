from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/create/{todo}")
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
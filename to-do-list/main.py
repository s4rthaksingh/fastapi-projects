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
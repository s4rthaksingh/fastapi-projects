from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Coffee(BaseModel):
    id : int
    name : str
    origin: str

coffees: List[Coffee] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to coffee house"}

@app.get("/coffees")
def get_coffees():
    return coffees

@app.post("/coffees")
def add_coffee(coffee: Coffee):
    coffees.append(coffee)
    return coffees

@app.put("/coffees/{coffee_id}")
def update_coffee(coffee_id: int, updated_coffee: Coffee):
    for i,c in enumerate(coffees):
        if c.id == coffee_id:
            coffees[i] = updated_coffee
            return updated_coffee
    return {"error": "Coffee not found"}

@app.delete("/coffees/{coffee_id}")
def delete_coffee(coffee_id):
    newcoffees:List[Coffee] = []
    for i,c in enumerate(coffees):
        if coffees[i] == coffee_id:
            continue
        else:
            newcoffees.append(c)
    return coffees

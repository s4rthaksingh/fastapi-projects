from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id : int
    name : str
    origin: str

teas: List[Tea] = []


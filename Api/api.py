from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create/")
async def create(item: Item):
    return item
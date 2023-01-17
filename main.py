from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if(published):
        return {'data' : f'{limit} published blogs from db'}
    else:
        return {'data' : f'{limit} blogs from db'}



@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    return {"data" : f"Blog is created with title as {request.title}"}
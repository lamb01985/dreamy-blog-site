from datetime import date
from pydantic import BaseModel


class PostCreate(BaseModel):
    author: str
    title: str
    body: str
    posted_date: date


class PostOut(PostCreate):
    id: int 

# TODO: Please write a Pydantic model to be used when creating a new post

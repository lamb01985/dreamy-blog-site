from datetime import date
from pydantic import BaseModel


class PostOut(BaseModel):
    id: int
    author: str
    title: str
    body: str
    posted_date: date


# TODO: Please write a Pydantic model to be used when creating a new post

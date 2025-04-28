from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from schemas import PostOut
import db

app = FastAPI()


@app.get("/api/posts")
async def get_posts() -> list[PostOut]:
    return db.get_posts()


@app.get("/api/posts/{post_id}")
async def get_post(post_id: int) -> PostOut:
    post = db.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail='Item not found')
    return post

# TODO: Implement a route which:
# - Accepts a POST request to "/api/posts"
# - Expects the fields of a post to be present in the request body
# - Calls the database function which will insert a new post
# - Returns the new post


# Route to handle requests for static assets
# this is a catch all so it should be registered last
@app.get('/{file_path}', response_class=FileResponse)
def get_static_file(file_path: str):
    if Path('static/' + file_path).is_file():
        return 'static/' + file_path
    raise HTTPException(status_code=404, detail='Item not found')

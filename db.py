from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import DBPost
from schemas import PostOut, PostCreate

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/blog"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_posts() -> list[PostOut]:
    db = SessionLocal()
    db_posts = db.query(DBPost).order_by(DBPost.posted_date).all()
    posts = []
    for db_post in db_posts:
        posts.append(
            PostOut(
                id=db_post.id,
                author=db_post.author,
                title=db_post.title,
                body=db_post.body,
                posted_date=db_post.posted_date,
            )
        )
    db.close()
    return posts


def get_post(post_id: int) -> PostOut | None:
    db = SessionLocal()
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post is None:
        return None
    post = PostOut(
        id=db_post.id,
        author=db_post.author,
        title=db_post.title,
        body=db_post.body,
        posted_date=db_post.posted_date,
    )
    db.close()
    return post


def create_post(post: PostCreate) -> PostOut:
    db = SessionLocal()
    db_post = DBPost (
        author = post.author, 
        title = post.title,
        body = post.body, 
        posted_date = post.posted_date,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db.close()
    return PostOut (
        id=db_post.id,
        author=db_post.author,
        title=db_post.title,
        body=db_post.body,
        posted_date=db_post.posted_date
    )

# TODO: Implement this function
# 1) Provide a type hint for the post parameter of the function
# 2) Create a db model object
# 2) Add it to the database
# 3) Refresh the db model and then return it as a PostOut

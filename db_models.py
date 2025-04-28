from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBPost(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    posted_date = Column(Date, nullable=False)

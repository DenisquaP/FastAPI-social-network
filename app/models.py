from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)

    posts = relationship('Post', back_populates="user")
    likes = relationship('Likes', back_populates='user')


class Post(Base):
    __tablename__ = 'post'
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)

    user = relationship('User', back_populates="posts")
    likes = relationship('Likes', back_populates='post')


class Likes(Base):
    __tablename__ = 'like'

    like_id = Column(
                    Integer,
                    primary_key=True,
                    nullable=False,
                    autoincrement=True
                    )
    post_id = Column(Integer, ForeignKey(Post.id))
    user_id = Column(Integer, ForeignKey(User.id))
    liked = Column(Boolean)
    disliked = Column(Boolean)

    post = relationship('Post', back_populates='likes')
    user = relationship('User', back_populates='likes')

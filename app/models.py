from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)

    posts = relationship('Post', back_populates="user")
    likes = relationship('Likes', back_populates='like')
    dislike = relationship('Likes', back_populates='dislike')


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
    liked = Column(Integer, ForeignKey(User.id))
    disliked = Column(Integer, ForeignKey(User.id))

    post = relationship('Post', back_populates='likes')
    like = relationship('User', back_populates='likes')
    dislike = relationship('User', back_populates='dislikes')

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from posts.schemas.post import (
    PostSchemaCreate,
    PostSchemaGet,
    PostSchemaUpdate
)
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from database import get_async_session
from models import User, Post
from auth.base_config import current_user
from typing import List

posts_router = APIRouter()


@posts_router.post(
                    '/create_post',
                    tags=['post'],
                    status_code=201,
                    response_model=PostSchemaCreate
                       )
async def create_post(
                body: PostSchemaCreate,
                db: AsyncSession = Depends(get_async_session),
                current_user: User = Depends(current_user)
                ):

    title = body.title
    text = body.text
    print(title, text, current_user.id)

    post = Post(
        user_id=current_user.id,
        title=title,
        text=text
    )

    db.add(post)
    await db.commit()

    return {'title': title, 'text': text}


@posts_router.get(
        '/get_posts',
        tags=['post'],
        response_model=List[PostSchemaGet],
        status_code=200
        )
async def get_posts(db: AsyncSession = Depends(get_async_session)):
    posts = await db.execute(select(Post))
    return posts.scalars().all()


@posts_router.get(
        '/get_user_posts',
        tags=['post'],
        response_model=List[PostSchemaGet],
        status_code=200
        )
async def get_user_posts(
                        db: AsyncSession = Depends(get_async_session),
                        current_user: User = Depends(current_user)
                    ):
    posts = await db.execute(select(Post).filter(
        Post.user_id == current_user.id
        ))
    return posts.scalars().all()


@posts_router.delete(
    '/delete_post',
    tags=['post'],
    status_code=200
)
async def delete_post(
                post_id: int,
                db: AsyncSession = Depends(get_async_session),
                current_user: User = Depends(current_user)
):
    try:
        post = await db.execute(select(Post).filter(
            Post.user_id == current_user.id,
            Post.id == post_id
            ))
        await db.delete(post.scalar_one())
        await db.commit()
        return {'status': f'Post {post_id} was deleted'}
    except NoResultFound:
        return {'status': f'Post {post_id} does not exist'}


@posts_router.put(
    '/update_post',
    status_code=200,
    response_model=PostSchemaGet,
    tags=['post']
)
async def update_post(
    body: PostSchemaUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(current_user),
):
    try:
        post = await db.execute(select(Post).filter(
            Post.user_id == current_user.id,
            Post.id == body.id
            ))
        post = post.scalar_one()
        post.title = body.title
        post.text = body.text
        print(post.title)

        await db.commit()
        return post
    except NoResultFound:
        return {'status': f'Post {body.id} does not exist'}

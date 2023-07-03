from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException

from database import get_async_session
from auth.base_config import current_user
from models import (
    Likes,
    Post,
    User
)

like_router = APIRouter()


@like_router.post(
    '/like',
    status_code=201,
    tags=['estimate']
)
async def put_a_like(
    post_id: int,
    like: bool,
    dislike: bool,
    current_user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),

):
    if like is dislike:
        raise HTTPException(400)
    try:
        post = await db.execute(select(Post).filter(Post.id == post_id))
        post = post.scalar_one()
        if post.user_id == current_user.id:
            raise HTTPException(400, 'You can`t like your own posts')

        try:
            already_rated = await db.execute(select(Likes).filter(
                Likes.post_id == post_id,
                Likes.user_id == current_user.id
                ))
            already_rated = already_rated.scalar_one()
            if already_rated:
                raise HTTPException(400, 'You can`t put a like or dislike to the post twice')  # noqa 501
        except NoResultFound:
            like = Likes(
                post_id=post_id,
                user_id=current_user.id,
                liked=like,
                disliked=dislike
            )

            db.add(like)
            await db.commit()
            return like

    except NoResultFound:
        raise HTTPException(404, f'Post {post_id} not found')

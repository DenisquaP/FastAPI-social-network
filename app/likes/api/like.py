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
    '/like/{post_id}',
    status_code=201
)
async def put_a_like(
    post_id: int,
    like: bool,
    dislike: bool,
    current_user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),

):
    try:
        post = await db.execute(select(Post).filter(Post.id == post_id))
        post = post.scalar_one()
        if post.user_id == current_user.id:
            return HTTPException(400, 'You can`t like your own posts')

        already_rated = await db.execute(select(Likes).filter(
            Likes.post_id == post_id,
            Likes.user_id == current_user.id
            ))
        if already_rated.scalar_one():
            return {'status': f'have you already evaluated post {post_id}'}

        like = Likes(post_id, current_user.user_id, liked=True, disliked=False)

        db.add(like)
        await db.commit()
        return {'status': f'you have liked the post {post_id}'}
    except NoResultFound:
        return HTTPException(404, f'Post {post_id} not found')

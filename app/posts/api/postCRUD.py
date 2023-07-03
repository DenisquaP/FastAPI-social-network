from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from posts.schemas.post import PostSchemaCreate
from sqlalchemy.future import select

from database import get_async_session
from models import User, Post
from auth.base_config import current_user

posts_router = APIRouter()


@posts_router.post(
                    '/create_post/',
                    tags=['post']
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


@posts_router.get('/get_posts/')
async def get_posts(db: AsyncSession = Depends(get_async_session)):
    posts = await db.execute(select(Post))
    return posts

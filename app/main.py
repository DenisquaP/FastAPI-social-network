from fastapi import FastAPI
from posts.api.postCRUD import posts_router
from likes.api.like import like_router

from auth.schemas import UserRead, UserCreate
from auth.base_config import auth_backend

from auth.base_config import fastapi_users

app = FastAPI(
    title='Social Network'
)

app.include_router(posts_router)
app.include_router(like_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

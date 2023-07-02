from fastapi import FastAPI
from API.main_router import router

app = FastAPI(
    title='Social Network'
)

app.include_router(router)

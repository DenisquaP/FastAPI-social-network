from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine
)

from settings import settings

engine = create_async_engine(
    settings.database_url
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autocommit=False,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session

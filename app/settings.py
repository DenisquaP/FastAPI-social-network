from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 8000

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/social_network_db"  # noqa 501


settings = Settings()

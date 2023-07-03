from fastapi_users import schemas
from pydantic import EmailStr, validator


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    @validator
    @classmethod
    def validate_email(cls, email):
        # Here I could validate email if I had a corporate email)
        # But i haven`t
        return True

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str

from pydantic import BaseModel


class PostSchemaCreate(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class PostSchemaUpdate(BaseModel):
    id: int
    title: str
    text: str

    class Config:
        orm_mode = True


class PostSchemaGet(BaseModel):
    user_id: int
    id: int
    title: str
    text: str

    class Config:
        orm_mode = True

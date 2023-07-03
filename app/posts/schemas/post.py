from pydantic import BaseModel


class PostSchemaCreate(BaseModel):
    title: str
    text: str

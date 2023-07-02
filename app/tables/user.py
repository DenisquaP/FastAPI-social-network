from sqlalchemy import (
    Column,
    Integer,
    String
)
from tables.base import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

from sqlalchemy import Column, DateTime, String, Uuid

from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Uuid, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    last_login = Column(DateTime)
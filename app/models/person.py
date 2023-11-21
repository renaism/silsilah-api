from sqlalchemy import Column, Date, String, Uuid
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Person(BaseModel):
    __tablename__ = "person"

    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    birth_place = Column(String)
    birth_date = Column(Date)
    decease_place = Column(String)
    decease_date = Column(Date)
    photo = Column(String)
    parent_family_id = Column(Uuid)

    parent_family = relationship("Family", foreign_keys=[parent_family_id])
from sqlalchemy import Column, ForeignKey, Uuid
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Family(BaseModel):
    __tablename__ = "family"

    id = Column(Uuid, primary_key=True, index=True)
    father_id = Column(Uuid, ForeignKey("person.id"))
    mother_id = Column(Uuid, ForeignKey("person.id"))

    father = relationship("Person", foreign_keys=[father_id])
    mother = relationship("Person", foreign_keys=[mother_id])
from sqlalchemy import Column, ForeignKey, Uuid
from sqlalchemy.orm import relationship

from app.dependencies.database import Base
from app.models.mixins.timestamp import TimestampMixin


class Family(TimestampMixin, Base):
    __tablename__ = "family"

    id = Column(Uuid, primary_key=True, index=True)
    father_id = Column(Uuid, ForeignKey("person.id"))
    mother_id = Column(Uuid, ForeignKey("person.id"))

    father = relationship("Person", foreign_keys=[father_id])
    mother = relationship("Person", foreign_keys=[mother_id])
    children = relationship(
        "Person",
        foreign_keys="Person.parent_family_id",
        order_by="Person.birth_date.asc()",
        back_populates="parent_family"
    )
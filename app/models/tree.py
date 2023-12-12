from sqlalchemy import Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship

from app.dependencies.database import Base
from app.models.mixins.timestamp import TimestampMixin


class Tree(TimestampMixin, Base):
    __tablename__ = "tree"

    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String)
    root_family_id = Column(Uuid, ForeignKey("family.id"))

    root_family = relationship("Family", foreign_keys=[root_family_id])
    
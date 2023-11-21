from sqlalchemy import Column, DateTime, ForeignKey, Uuid
from sqlalchemy.orm import relationship

from app.database import Base


class BaseModel(Base):
    created_on = Column(DateTime)
    edited_on = Column(DateTime)
    deleted_on = Column(DateTime)

    created_by = Column(Uuid, ForeignKey("user.id"))
    edited_by = Column(Uuid, ForeignKey("user.id"))
    deleted_by = Column(Uuid, ForeignKey("user.id"))

    create_user = relationship("User", foreign_keys=[created_by], lazy=True)
    edit_user = relationship("User", foreign_keys=[edited_by], lazy=True)
    delete_user = relationship("User", foreign_keys=[deleted_by], lazy=True)
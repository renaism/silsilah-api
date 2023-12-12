from sqlalchemy import Column, DateTime, ForeignKey, Uuid
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship


class TimestampMixin(object):
    created_on = Column(DateTime)
    edited_on = Column(DateTime)
    deleted_on = Column(DateTime)

    created_by = Column(Uuid, ForeignKey("user.id"))
    edited_by = Column(Uuid, ForeignKey("user.id"))
    deleted_by = Column(Uuid, ForeignKey("user.id"))

    @declared_attr
    def create_user(cls):
        return relationship("User", foreign_keys=[cls.created_by], lazy=True)
    
    @declared_attr
    def edit_user(cls):
        return relationship("User", foreign_keys=[cls.edited_by], lazy=True)
    
    @declared_attr
    def delete_user(cls):
        return relationship("User", foreign_keys=[cls.deleted_by], lazy=True)
from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID

from app.models import Person


class PersonController:
    @staticmethod
    def get(db: Session, id: UUID) -> Person:
        stmt = select(Person) \
            .where(Person.id == id) \
            .where(Person.deleted_on == None)
        
        person = db.scalars(stmt).first()
        
        return person
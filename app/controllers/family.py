from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID

from app.models import Family


class FamilyController:
    @staticmethod
    def get(db: Session, id: UUID) -> Family:
        stmt = select(Family) \
            .where(Family.id == id) \
            .where(Family.deleted_on == None)
        
        family = db.scalars(stmt).first()
        
        return family
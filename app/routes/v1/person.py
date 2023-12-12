from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.dependencies.database import get_db
from app.controllers import PersonController
from app.models import Person
from app.schemas import PersonSchema


router = APIRouter(
    prefix="/api/v1/person",
    tags=["person"]
)


def get_person(id: UUID, db: Session = Depends(get_db)) -> Person:
    person = PersonController.get(db, id)

    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Person not found"
        )
    
    return person


@router.get("/{id}", response_model=PersonSchema)
def get(person: Person = Depends(get_person)) -> Person:
    return person
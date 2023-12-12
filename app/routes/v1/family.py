from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.dependencies.database import get_db
from app.controllers import FamilyController
from app.models import Family
from app.schemas import FamilySchema


router = APIRouter(
    prefix="/api/v1/family",
    tags=["family"]
)


def get_family(id: UUID, db: Session = Depends(get_db)) -> Family:
    family = FamilyController.get(db, id)

    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Family not found"
        )
    
    return family


@router.get("/{id}", response_model=FamilySchema)
def get(family: Family = Depends(get_family)) -> Family:
    return family
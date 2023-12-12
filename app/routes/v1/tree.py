from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.dependencies.database import get_db
from app.controllers import TreeController
from app.models import Tree
from app.schemas import FamilyTreeSchema, TreeSchema


router = APIRouter(
    prefix="/api/v1/tree",
    tags=["tree"]
)


def get_tree(id: UUID, db: Session = Depends(get_db)) -> Tree:
    tree = TreeController.get(db, id)

    if not tree:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tree not found"
        )
    
    return tree


@router.get("/{id}", response_model=TreeSchema)
def get(tree: Tree = Depends(get_tree)) -> Tree:
    return tree


@router.get("/{id}/family_tree", response_model=FamilyTreeSchema)
def get_family_tree(tree: Tree = Depends(get_tree), db: Session = Depends(get_db)) -> dict:
    ft = TreeController.get_family_tree(db, tree.root_family)

    return ft
    
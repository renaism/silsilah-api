from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from uuid import UUID

from app.models import Family, Person, Tree


class TreeController:
    @staticmethod
    def get(db: Session, id: UUID) -> Tree:
        stmt = select(Tree) \
            .where(Tree.id == id) \
            .where(Tree.deleted_on == None)
        
        tree = db.scalars(stmt).first()
        
        return tree
    
    
    @staticmethod
    def get_family_tree(db: Session, person: Person) -> dict:
        family_tree = person.__dict__

        # Get family data of the person
        stmt = select(Family) \
            .where(Family.deleted_on == None)
        
        if person.gender == "m":
            stmt = stmt.where(Family.father_id == person.id)
        else:
            stmt = stmt.where(Family.mother_id == person.id)
        
        family = db.scalars(stmt).first()
        
        if family:
            family_tree["family_id"] = family.id

            # Get the spouse of the person
            family_tree["spouse"] = family.mother if person.gender == "m" else family.father

            # Get the children of the person
            family_tree["children"] = list(map(
                lambda c: TreeController.get_family_tree(db, c),
                family.children
            ))
        else:
            family_tree["family_id"] = None
            family_tree["spouse"] = None
            family_tree["children"] = []

        return family_tree
            
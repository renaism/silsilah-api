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
    def get_family_tree(db: Session, family: Family) -> dict:
        def get_family(db: Session, person: Person) -> dict:
            family_data = {
                "family_id": None,
                "spouse": None,
                "children": []
            }

            stmt = select(Family) \
                .where(Family.deleted_on == None)
            
            if person.gender == "m":
                stmt = stmt.where(Family.father_id == person.id)
            else:
                stmt = stmt.where(Family.mother_id == person.id)
            
            family = db.scalars(stmt).first()

            if family:
                family_data["family_id"] = family.id

                if person.gender == "m":
                    family_data["spouse"] = family.mother
                else:
                    family_data["spouse"] = family.father
                
                for child in family.children:
                    child_family_data = get_family(db, child)
                    child_data = child.__dict__
                    child_data["family_id"] = child_family_data["family_id"]
                    child_data["spouse"] = child_family_data["spouse"]
                    child_data["children"] = child_family_data["children"]
                
                    family_data["children"].append(child_data)
            
            return family_data

        family_tree = {
            "root_family_id": family.id,
            "root_father": family.father,
            "root_mother": family.mother,
            "children": []
        }

        for child in family.children:
            child_family_data = get_family(db, child)
            child_data = child.__dict__
            child_data["family_id"] = child_family_data["family_id"]
            child_data["spouse"] = child_family_data["spouse"]
            child_data["children"] = child_family_data["children"]

            family_tree["children"].append(child_data)
        
        return family_tree
            
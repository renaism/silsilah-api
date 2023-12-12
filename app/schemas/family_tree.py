from pydantic import BaseModel
from typing import Any
from uuid import UUID

from app.schemas.person import PersonSchema


class PersonTreeSchema(PersonSchema):
    family_id: UUID | None
    spouse: PersonSchema | None
    children: list[PersonSchema]


class FamilyTreeSchema(BaseModel):
    root_family_id: UUID
    root_father: PersonSchema
    root_mother: PersonSchema
    children: list[PersonTreeSchema]

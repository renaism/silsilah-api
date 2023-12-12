from pydantic import BaseModel
from uuid import UUID

from app.schemas.person import PersonSchema


class FamilySchema(BaseModel):
    id: UUID
    father: PersonSchema
    mother: PersonSchema
    children: list[PersonSchema]

    class Config:
        from_attributes = True
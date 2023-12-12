from pydantic import BaseModel
from uuid import UUID

from app.schemas.family import FamilySchema


class TreeSchema(BaseModel):
    id: UUID
    name: str
    root_family: FamilySchema

    class Config:
        from_attributes = True
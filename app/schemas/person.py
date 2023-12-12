from datetime import date
from pydantic import BaseModel
from uuid import UUID


class PersonSchema(BaseModel):
    id: UUID
    name: str
    gender: str
    birth_place: str | None
    birth_date: date | None
    decease_place: str | None
    decease_date: date | None
    photo: str | None
    parent_family_id: UUID | None

    class Config:
        from_attributes = True
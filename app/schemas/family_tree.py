from __future__ import annotations
from pydantic import BaseModel
from typing import Any
from uuid import UUID

from app.schemas.person import PersonSchema


class FamilyTreeSchema(PersonSchema):
    family_id: UUID | None
    spouse: PersonSchema | None
    children: list[FamilyTreeSchema]

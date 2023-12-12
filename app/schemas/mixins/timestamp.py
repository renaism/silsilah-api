from datetime import datetime
from uuid import UUID


class TimestampMixinSchema(object):
    created_on: datetime | None
    edited_on: datetime | None
    deleted_on: datetime | None

    created_by: UUID | None
    edited_by: UUID | None
    deleted_by: UUID | None
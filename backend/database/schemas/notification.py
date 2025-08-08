

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class NotificationRead(BaseModel):
    id: UUID
    user_id: UUID
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        orm_mode = True
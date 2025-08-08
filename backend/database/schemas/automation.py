

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class AutomationBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    config_schema: Optional[dict] = None


class AutomationCreate(AutomationBase):
    pass


class AutomationRead(AutomationBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
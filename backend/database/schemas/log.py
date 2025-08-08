

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class LogRead(BaseModel):
    id: UUID
    workflow_id: UUID
    step_id: Optional[UUID]
    status: str
    input: Optional[dict] = None
    output: Optional[dict] = None
    error_message: Optional[str] = None
    executed_at: datetime

    class Config:
        orm_mode = True
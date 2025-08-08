

from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime


class StepBase(BaseModel):
    name: str
    step_order: Optional[int]
    type: str  # 'manual' ou 'automation'
    config: Optional[dict] = None


class StepCreate(StepBase):
    pass


class StepRead(StepBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class WorkflowBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "active"


class WorkflowCreate(WorkflowBase):
    steps: Optional[List[StepCreate]] = []


class WorkflowRead(WorkflowBase):
    id: UUID
    created_at: datetime
    steps: List[StepRead] = []

    class Config:
        orm_mode = True
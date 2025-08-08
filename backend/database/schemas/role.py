

from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class RoleBase(BaseModel):
    name: str
    permissions: Optional[dict] = None


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase):
    id: UUID

    class Config:
        orm_mode = True
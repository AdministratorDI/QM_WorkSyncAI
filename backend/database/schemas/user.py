

from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: Optional[str] = "user"
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserRead(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class UserSettingsRead(BaseModel):
    language: Optional[str] = "pt-PT"
    timezone: Optional[str] = "Europe/Lisbon"
    preferences: Optional[dict] = None

    class Config:
        orm_mode = True
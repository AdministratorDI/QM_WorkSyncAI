

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SuggestionBase(BaseModel):
    title: str
    description: Optional[str] = None

class SuggestionCreate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.suggestions import SuggestionCreate, SuggestionResponse
from app.models import suggestions as models

router = APIRouter(prefix="/suggestions", tags=["Suggestions"])

@router.post("/", response_model=SuggestionResponse, status_code=status.HTTP_201_CREATED)
def create_suggestion(suggestion: SuggestionCreate, db: Session = Depends(get_db)):
    db_suggestion = models.Suggestion(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

@router.get("/", response_model=list[SuggestionResponse])
def get_suggestions(db: Session = Depends(get_db)):
    return db.query(models.Suggestion).all()

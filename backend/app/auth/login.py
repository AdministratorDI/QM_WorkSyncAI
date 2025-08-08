

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from backend.database.models.user import User
from backend.database.schemas.user import UserRead
from pydantic import BaseModel
import hashlib

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login", response_model=UserRead)
def login(request: LoginRequest, db: Session = Depends(get_db), lang: str = "pt"):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        detail = "Credenciais inválidas." if lang == "pt" else "Invalid credentials."
        raise HTTPException(status_code=401, detail=detail)

    hashed_input = hashlib.sha256(request.password.encode()).hexdigest()
    if hashed_input != user.password_hash:
        detail = "Credenciais inválidas." if lang == "pt" else "Invalid credentials."
        raise HTTPException(status_code=401, detail=detail)

    return user
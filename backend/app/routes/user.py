

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from backend.database.database import SessionLocal
from backend.database.models.user import User
from backend.database.schemas.user import UserCreate, UserRead
import uuid
import hashlib

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# Dependency para obter sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db), lang: str = "pt"):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        detail = "Email já registado." if lang == "pt" else "Email already registered."
        raise HTTPException(status_code=400, detail=detail)

    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    new_user = User(
        id=uuid.uuid4(),
        email=user.email,
        password_hash=hashed_password,
        full_name=user.full_name,
        role=user.role,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        detail = "Utilizador não encontrado." if lang == "pt" else "User not found."
        raise HTTPException(status_code=404, detail=detail)
    return user
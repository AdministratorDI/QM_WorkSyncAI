from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.database.database import SessionLocal
from app.database.models.log import Log
from app.database.schemas.log import LogRead

router = APIRouter(
    prefix="/logs",
    tags=["logs"]
)

# Dependência para obter a sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[LogRead])
def list_logs(db: Session = Depends(get_db)):
    return db.query(Log).all()


@router.get("/{log_id}", response_model=LogRead)
def get_log(log_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    log = db.query(Log).filter(Log.id == log_id).first()
    if not log:
        detail = "Log não encontrado." if lang == "pt" else "Log not found."
        raise HTTPException(status_code=404, detail=detail)
    return log


@router.get("/by_workflow/{workflow_id}", response_model=List[LogRead])
def get_logs_by_workflow(workflow_id: UUID, db: Session = Depends(get_db)):
    return db.query(Log).filter(Log.workflow_id == workflow_id).all()
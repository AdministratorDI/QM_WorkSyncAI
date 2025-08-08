

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from backend.database.database import SessionLocal
from backend.database.models.notification import Notification
from backend.database.schemas.notification import NotificationRead

from datetime import datetime

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

# Dependência para obter sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[NotificationRead])
def list_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).order_by(Notification.created_at.desc()).all()


@router.get("/{notification_id}", response_model=NotificationRead)
def get_notification(notification_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    notif = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notif:
        detail = "Notificação não encontrada." if lang == "pt" else "Notification not found."
        raise HTTPException(status_code=404, detail=detail)
    return notif


@router.put("/{notification_id}/read", response_model=NotificationRead)
def mark_as_read(notification_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    notif = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notif:
        detail = "Notificação não encontrada." if lang == "pt" else "Notification not found."
        raise HTTPException(status_code=404, detail=detail)
    notif.is_read = True
    db.commit()
    db.refresh(notif)
    return notif


@router.delete("/{notification_id}")
def delete_notification(notification_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    notif = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notif:
        detail = "Notificação não encontrada." if lang == "pt" else "Notification not found."
        raise HTTPException(status_code=404, detail=detail)
    db.delete(notif)
    db.commit()
    return {"message": "Notificação eliminada com sucesso." if lang == "pt" else "Notification successfully deleted."}
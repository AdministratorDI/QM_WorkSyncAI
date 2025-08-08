from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from backend.database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(String, default='user')
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    settings = relationship("UserSettings", back_populates="user", uselist=False)
    notifications = relationship("Notification", back_populates="user", cascade="all, delete")
    workflows = relationship("Workflow", back_populates="user", cascade="all, delete")


class UserSettings(Base):
    __tablename__ = 'user_settings'
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    language = Column(String, default='pt-PT')
    timezone = Column(String, default='Europe/Lisbon')
    preferences = Column(String)  # ou JSON, se preferires

    user = relationship("User", back_populates="settings")


class UserRole(Base):
    __tablename__ = 'user_roles'
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)
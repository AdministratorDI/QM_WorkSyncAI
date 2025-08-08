from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class UserRole(enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    totp_secret = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)
    created_at = Column(DateTime, default=datetime.utcnow)

class Workflow(Base):
    __tablename__ = 'workflows'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    trigger = Column(String(100), nullable=False)
    action = Column(String(100), nullable=False)
    condition = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", backref="workflows")

    logs = relationship("ExecutionLog", back_populates="workflow", cascade="all, delete")

class ExecutionLog(Base):
    __tablename__ = 'execution_logs'

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey('workflows.id'), nullable=False)
    executed_at = Column(DateTime, default=datetime.utcnow)
    result = Column(String(255), nullable=False)
    suggestion = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)

    workflow = relationship("Workflow", back_populates="logs")

__all__ = ["User", "Workflow", "ExecutionLog", "UserRole"]

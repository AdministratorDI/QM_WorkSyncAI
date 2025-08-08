

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from backend.database.database import Base


class Workflow(Base):
    __tablename__ = 'workflows'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default='active')
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workflows")
    steps = relationship("Step", back_populates="workflow", cascade="all, delete")


class Step(Base):
    __tablename__ = 'steps'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workflow_id = Column(UUID(as_uuid=True), ForeignKey('workflows.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    step_order = Column(Integer)
    type = Column(String, nullable=False)  # 'automation' ou 'manual'
    config = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    workflow = relationship("Workflow", back_populates="steps")
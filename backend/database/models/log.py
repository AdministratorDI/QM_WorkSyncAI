

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from backend.database.database import Base


class Log(Base):
    __tablename__ = 'logs'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workflow_id = Column(UUID(as_uuid=True), ForeignKey('workflows.id', ondelete='CASCADE'))
    step_id = Column(UUID(as_uuid=True), ForeignKey('steps.id', ondelete='SET NULL'))
    status = Column(String, nullable=False)  # 'success', 'error', 'pending'
    input = Column(JSON)
    output = Column(JSON)
    error_message = Column(String)
    executed_at = Column(DateTime, default=datetime.utcnow)
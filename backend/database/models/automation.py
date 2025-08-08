

from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from backend.database.database import Base


class Automation(Base):
    __tablename__ = 'automations'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    config_schema = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from backend.database.database import Base


class Role(Base):
    __tablename__ = 'roles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    permissions = Column(JSON)
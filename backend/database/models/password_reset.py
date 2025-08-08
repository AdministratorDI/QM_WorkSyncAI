

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from backend.database.database import Base


class PasswordResetToken(Base):
    __tablename__ = 'password_reset_tokens'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
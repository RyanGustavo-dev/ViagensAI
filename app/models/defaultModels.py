import uuid
from app.extension import db
from datetime import datetime
from sqlalchemy import Column, DateTime, UUID

class TableDefault(db.Model):
    __tablename__ = "inital_default"
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime)
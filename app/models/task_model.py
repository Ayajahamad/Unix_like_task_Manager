from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base
from datetime import datetime
from sqlalchemy import Column, DateTime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # ⬅️ changed from 'name'
    description = Column(String, nullable=True)  # ⬅️ add this
    status = Column(String, default="running")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed = Column(Boolean, default=False)


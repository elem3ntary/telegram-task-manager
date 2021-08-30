from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.sqltypes import Date
from app.db.connection import Base
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    processing = "processing"
    assignet = "assignet"
    done = "done"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True)
    chat_id = Column(Integer, index=True)
    assignet_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    due_at = Column(DateTime, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.assignet)
    assignet_by = Column(Integer)

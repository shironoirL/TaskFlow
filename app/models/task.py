import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.base import TimeStampMixin


class TaskStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class Task(TimeStampMixin, Base):
    __tablename__ = "tasks"

    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(TaskStatus), default=TaskStatus.OPEN, nullable=False)
    assignee_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    project_id = Column(
        Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )

    assignee = relationship("User", backref="tasks")
    project = relationship("Project", backref="tasks")

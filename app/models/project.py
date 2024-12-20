from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.base import TimeStampMixin


class Project(TimeStampMixin, Base):
    __tablename__ = "projects"

    name = Column(String)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner = relationship("User", back_populates="projects")

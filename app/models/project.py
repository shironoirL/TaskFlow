from sqlalchemy import Column, String, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base import TimeStampMixin
from app.core.db import Base


class Project(TimeStampMixin, Base):
    __tablename__ = "projects"

    name = Column(String)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner = relationship("User", back_populates="projects")

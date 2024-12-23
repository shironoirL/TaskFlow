from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.base import TimeStampMixin


class User(TimeStampMixin, Base):
    __tablename__ = "users"

    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

    projects = relationship("Project", back_populates="owner")

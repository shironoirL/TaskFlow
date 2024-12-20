from sqlalchemy import Column, String
from app.models.base import TimeStampMixin
from app.core.db import Base


class User(TimeStampMixin, Base):
    __tablename__ = "users"

    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

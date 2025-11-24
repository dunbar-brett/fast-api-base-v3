# External Dependencies
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Current App
from todo_app.db.connector import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)

    items = relationship("Item", back_populates="user", cascade="all, delete-orphan")

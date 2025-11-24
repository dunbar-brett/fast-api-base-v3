# External Dependencies
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Current App
from todo_app.db.connector import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User", back_populates="items")

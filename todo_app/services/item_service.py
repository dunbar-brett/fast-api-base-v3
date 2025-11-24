# Standard Library
from typing import List

# External Dependencies
from sqlalchemy.orm import Session

# Current App
from todo_app.models.item import Item
from todo_app.models.user import User


def create_item(db: Session, user_id: int, title: str, description: str | None) -> Item:
    # check user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    item = Item(title=title, description=description, user_id=user_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_items_for_user(db: Session, user_id: int) -> List[Item]:
    return db.query(Item).filter(Item.user_id == user_id).all()


def list_items(db: Session) -> List[Item]:
    return db.query(Item).all()

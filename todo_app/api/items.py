# Standard Library
from typing import List

# External Dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Current App
from todo_app.db.connector import get_db
from todo_app.schemas.item import ItemCreate, ItemOut
from todo_app.services.item_service import create_item, list_items, list_items_for_user

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def add_item(payload: ItemCreate, db: Session = Depends(get_db)):
    try:
        item = create_item(db, payload.user_id, payload.title, payload.description)
        return item
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.get("/user/{user_id}", response_model=List[ItemOut])
def get_users_items(user_id: int, db: Session = Depends(get_db)):
    items = list_items_for_user(db, user_id)
    return items


@router.get("/all", response_model=List[ItemOut])
def get_all_items(db: Session = Depends(get_db)):
    items = list_items(db)
    return items

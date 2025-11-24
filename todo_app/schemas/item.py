# Standard Library
from typing import Optional

# External Dependencies
from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None


class ItemOut(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)

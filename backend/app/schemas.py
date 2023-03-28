# importing modules
from typing import List, Optional
from sqlmodel import Field
from pydantic import BaseModel
from datetime import datetime
from datetime import date

# Creating data schemas to use by particular API methods (to create and update data)

class BookCreate(BaseModel):
    author: str
    title: str

class BookUpdate(BaseModel):
    book_id: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None

class UserCreate(BaseModel):
    name: str
    password: str

class UserUpdate(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None

class RentUpdate(BaseModel):
    rent_id: Optional[str] = None
    book_id: Optional[str] = None
    user_id: Optional[str] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None

class RentCreate(BaseModel):
    name: str
    author: str
    title: str
    start_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    due_date: datetime = Field(default_factory=None, nullable=True)
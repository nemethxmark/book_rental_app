# importing modules
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
# ----------------------------------------------------------------------------------------------------------------------

# Creating data models (to organize related data and define how it is stored in the database) necessary for the application

class Book(SQLModel, table=True):
    book_id: str = Field(default=None, primary_key=True)
    author: str
    title: str

class User(SQLModel, table=True):
    user_id: str = Field(default=None, primary_key=True)
    name: str
    password: str

class Rent(SQLModel, table=True):
    rent_id: str = Field(default=None, primary_key=True)
    user_id: str
    name: str
    book_id: str
    author: str
    title: str
    start_date: datetime
    due_date: datetime
# importing modules
import sqlalchemy
from fastapi import FastAPI, Query, HTTPException, APIRouter
from sqlmodel import SQLModel, create_engine, Session
from .schemas import *
from .database import engine
from app.routers.users import user_router
from app.routers.events import rent_router
from app.routers.books import book_router
from fastapi_sqlalchemy import DBSessionMiddleware
# ----------------------------------------------------------------------------------------------------------------------

# function to create the database file with the predefined data structures
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# creating the FastApi instance, the main point of interact to create all API
app = FastAPI()

# importing routers (complexitiy is divided)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(rent_router)

# creating a middleware layer
app.add_middleware(DBSessionMiddleware, db_url="sqlite:///app/database.db")

# path operation to create the database file, if it does not already exist when the server is being started
@app.on_event("startup")
def on_startup():
    if not sqlalchemy.inspect(engine).has_table('user'):
        create_db_and_tables()
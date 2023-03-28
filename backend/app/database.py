# importing modules
from sqlmodel import SQLModel, create_engine, Session
# ----------------------------------------------------------------------------------------------------------------------

# database (SQL) file path to store data
database_file_path = "app/database.db"
sqlite_url = f"sqlite:///{database_file_path}"
# creating a sqlite engine and connecting to the database
engine = create_engine(sqlite_url, echo=True)
# creating an engine, with only one thread to communicate on with the database
connect_args = {"check_same_thread": False}
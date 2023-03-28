# importing modules
from fastapi import APIRouter, HTTPException, Query
from app.models import Book
from app.schemas import BookCreate,BookUpdate
from uuid import uuid4
from fastapi_sqlalchemy import db
from typing import List
# ----------------------------------------------------------------------------------------------------------------------

# creating a router for routing API requests
book_router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not Found!"}}
)

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@book_router.post("/post")
# path operation function to be called whenever it receives a request to the URL "/post" using a POST operation
def create_book(book_create: BookCreate):
    with db.session as sess:
        # converting input BookCreate to a Book model (pydantic)) by extending with the necessary data
        book = Book(**book_create.dict(), book_id=str(uuid4()))
        # conversion from pydantic model to a database record
        db_book = Book.from_orm(book)
        # adding the database record to the database
        sess.add(db_book)
        # saving and refreshing the database
        sess.commit()
        sess.refresh(db_book)
        # returning back the pydantic model
        return db_book

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@book_router.get("/get", response_model=List[Book])
# path operation function to be called whenever it receives a request to the URL "/get" using a GET operation
def read_books(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with db.session as sess:
        # query for fetching all books from the database with a limitation and an offset
        books = sess.query(Book).offset(offset).limit(limit).all()
        return books

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@book_router.get("/get_by_date", response_model=List[Book])
# path operation function to be called whenever it receives a request to the URL "/get_by_date" using a GET operation
def read_books_available_today():
    with db.session as sess:
        # querying Rent objects from the database, which has a due_date attribute bigger than today - still active rents
        rents = sess.query(Rent).filter(Rent.due_date > datetime.utcnow()).all()
        # loading actively rented book ids into a list
        now_rented_book_ids = []
        for rent in rents:
            now_rented_book_ids.append(rent.book_id)
        # filtering out duplicated objects
        now_rented_book_ids_set = set(now_rented_book_ids)
        # querying all Book objects from the database
        all_books = sess.query(Book).all()
        # loading all book ids into a list
        all_books_id = []
        for book in all_books:
            all_books_id.append(book.book_id)
        call_books_id_set = set(all_books_id)
        # all_book_id - actively_rented_books_id = available_books_id
        available_books_id = all_books_id_set.difference(now_rented_book_ids_set)
        # available book id
        available_books = []
        # querying available Book objects based on the ids of available books
        for available_book_id in available_books_id:
            # querying Book object matching one available book's id
            available_book = sess.query(Book).filter(Book.book_id == available_book_id).all()
            available_books.append(available_book[0])
        return available_books

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@book_router.patch("/update/{book_id}", response_model=Book)
# path operation function to be called whenever it receives a request to the URL "/update/{book_id}" using a PATCH operation
def update_book(book_id: str, book: BookUpdate):
    with db.session as sess:
        # querying for the book having the particular ID
        db_book = sess.get(Book, book_id)
        # if there is not any book having the particular ID - throw an Exception
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        # convert the pydantic model getting from the database to dictionary
        book_data = book.dict(exclude_unset=True)
        # updating the database record
        for key, value in book_data.items():
            setattr(db_book, key, value)
        # add the database record (or update) to the database, then save and refresh the database
        sess.add(db_book)
        sess.commit()
        sess.refresh(db_book)
        return db_book

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@book_router.delete("/delete/{book_id}")
# path operation function to be called whenever it receives a request to the URL "/delete/{book_id}" using a DELETE operation
def delete_book(book_id: str):
    with db.session as sess:
        # querying for the book having the particular ID
        book = sess.get(Book, book_id)
        # if there is not any book having the particular ID - throw an Exception
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        # delete the book with the particular id, save the database and sending the response to the client.
        sess.delete(book)
        sess.commit()
        response = {"ok": True}
        return response
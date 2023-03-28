# importing modules
from fastapi import APIRouter, HTTPException, Query
from app.models import *
from app.schemas import *
from uuid import uuid4
from fastapi_sqlalchemy import db
from typing import List, Optional
# ----------------------------------------------------------------------------------------------------------------------

# creating a router for routing API requests
rent_router = APIRouter(
    prefix="/rents",
    tags=["rents"],
    responses={404: {"description": "Not Found!"}}
)

# path operation (HTTP method to communicate with the API) for creating a rent instance
# path operator decorator
@rent_router.post("/post")
# path operation function to be called whenever it receives a request to the URL "/post" using a POST operation
def create_rent(rent_create: RentCreate):
    with db.session as sess:
        # convert the input, rent_create pydantic model (class object) to a dictionary
        rent_create_dict = rent_create.dict()
        # querying all Book objects from the database
        books = sess.query(Book).all()
        # creating a list to store ids of the matching books
        matching_books_id = []
        # collect id of all books from the database which has the same author and title as contained by the input
        for book in books:
            if book.author == rent_create_dict['author'] and book.title == rent_create_dict['title']:
                matching_books_id.append(book.book_id)
        # checking if a book exists (based on the id)
        if not matching_books_id:
            raise HTTPException(status_code=404, detail="The book is invalid, can not found in the database")
        # querying all active rents (due_date attribute is bigger than today)
        rents = sess.query(Rent).filter(Rent.due_date > datetime.utcnow()).all()
        # putting all rented book ids into a list
        now_rented_book_ids = []
        for rent in rents:
            now_rented_book_ids.append(rent.book_id)
        # filtering out duplicated objects
        now_rented_book_ids_set = set(now_rented_book_ids)
        matching_books_id_set = set(matching_books_id)
        # determining available books id with matching author and title
        available_matching_books_id = matching_books_id_set - now_rented_book_ids_set
        # checking if a book exists (based on the id)
        if not available_matching_books_id:
            raise HTTPException(status_code=404, detail="The book is not available (rented by somebody else) right now, please check what books are available")
        # querying all users from the database
        users = sess.query(User).all()
        # getting the user_id from the database, based on the username
        user_id = None
        for user in users:
            if user.name == rent_create_dict['name']:
                user_id = user.user_id
                break
        # if the user doesn't exist, throwing an exception
        if not user_id:
            raise HTTPException(status_code=404,detail="Invalid user, not found in the database")
        # creting a rent object based on the input object extended by some automatically generated ID
        rent = Rent(**rent_create.dict(), rent_id=str(uuid4()), user_id=user_id, book_id = list(available_matching_books_id)[0])
        # converting the model (class) to a database record (table)
        db_rent = Rent.from_orm(rent)
        # add the database record (or update) to the database, then save and refresh the database
        sess.add(db_rent)
        sess.commit()
        sess.refresh(db_rent)
        return db_rent

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@rent_router.get("/get", response_model=List[Rent])
# path operation function to be called whenever it receives a request to the URL "/get" using a GET operation
def read_rent(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with db.session as sess:
        # fetching all rents from the database with a limitation and an offset
        rent = sess.query(Rent).offset(offset).limit(limit).all()
    return rent

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@rent_router.get("/get_active", response_model=List[Rent])
# path operation function to be called whenever it receives a request to the URL "/get_active" using a GET operation
def read_rent(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with db.session as sess:
        # fetching all active rents from the database with a limitation and an offset
        rents = sess.query(Rent).filter(Rent.due_date > datetime.utcnow()).all()
    return rents


# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@rent_router.patch("/update/{rent_id}", response_model=Rent)
# path operation function to be called whenever it receives a request to the URL "/update/{rent_id}" using a PATCH operation
def update_rent(rent_id: str, rent: RentUpdate):
    with db.session as sess:
        # querying for the rent having the particular ID
        db_rent = sess.get(Rent, rent_id)
        # if there is not any rent having the particular ID - throw an Exception
        if not db_rent:
            raise HTTPException(status_code=404, detail="Rent not found")
        # convert the pydantic model getting from the database to dictionary
        rent_data = rent.dict(exclude_unset=True)
        # updating the database record
        for key, value in rent_data.items():
            setattr(db_rent, key, value)
        # add the database record (or update) to the database, then save and refresh the database
        sess.add(db_rent)
        sess.commit()
        sess.refresh(db_rent)
    return db_rent

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@rent_router.delete("/delete/{rent_id}")
# path operation function to be called whenever it receives a request to the URL "/delete/{rent_id}" using a DELETE operation
async def delete_rent(rent_id: str):
    with db.session as sess:
        # querying for the rent having the particular ID
        rent = sess.get(Rent, rent_id)
        # if there is not any rent having the given ID - throw an Exception
        if not rent:
            raise HTTPException(status_code=404, detail="Rent not found")
        # delete the rent with the particular id, save the database and sending the response to the client.
        sess.delete(rent)
        sess.commit()
        response = {"ok": True}
    return response



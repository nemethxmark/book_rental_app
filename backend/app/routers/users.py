# imporing modules
from fastapi import APIRouter, HTTPException, Query
from app.models import *
from app.schemas import *
from uuid import uuid4
from fastapi_sqlalchemy import db
from typing import List, Optional
# ----------------------------------------------------------------------------------------------------------------------

# creating a router for routing API requests
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not Found!"}}
)

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@user_router.post("/post")
# path operation function to be called whenever it receives a request to the URL "/post" using a POST operation
def create_user(user_create: UserCreate):
    with db.session as sess:
        # converting input UserCreate to a User model (pydantic))
        user_create_dict = user_create.dict()
        # hashing password including by the input
        hashed_password = get_password_hash(user_create_dict['password'])
        user_create_dict['password'] = hashed_password
        # creating the User model, by extending the input by an automatically generated ID
        user = User(**user_create_dict, user_id=str(uuid4()))
        # conversion from model (class) to a database record (table)
        db_user = User.from_orm(user)
        # querying all users from the database
        users = sess.query(User).all()
        # checking if the username want to be created is in use
        username_not_used = True
        for user_iterator in users:
            if user.name == user_iterator.name:
                username_not_used = False
        # if the username is free
        if username_not_used:
            # saving and refreshing the database
            sess.add(db_user)
            sess.commit()
            sess.refresh(db_user)
        return db_user


# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@user_router.get("/get", response_model=List[User])
# path operation function to be called whenever it receives a request to the URL "/get" using a POST operation
def read_user(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with db.session as sess:
        # query for fetching all users from the database with a limitation and an offset
        user = sess.query(User).offset(offset).limit(limit).all()
        return user

# @user_router.patch("/update/{user_id}", response_model=User)
# def update_user(user_id: str, user: UserUpdate, current_user: User = Depends(get_current_user)):
#     with db.session as sess:
#         if current_user.name != "admin":
#             raise HTTPException(status_code=401, detail="Unauthorized, only the admin can update a user!")
#         else:
#             db_user = sess.get(User, user_id)
#             if not db_user:
#                 raise HTTPException(status_code=404, detail="User not found")
#             if User.name == "admin":
#                 raise HTTPException(status_code=405, detail="Admin user can not be changed")
#             user_data = user.dict(exclude_unset=True)
#             for key, value in user_data.items():
#                 setattr(db_user, key, value)
#             sess.add(db_user)
#             sess.commit()
#             sess.refresh(db_user)
#             return db_user

# path operation (HTTP method to communicate with the API) for creating a book instance
# path operator decorator
@user_router.delete("/delete/{user_id}")
# path operation function to be called whenever it receives a request to the URL "/delete/{user_id}" using a POST operation
def delete_user(user_id: str):
    with db.session as sess:
        # querying for the user having the particular ID
        user = sess.get(User, user_id)
        # if there is not any user having the particular ID - throw an Exception
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # the admin user can't be deleted
        if user.name == "admin":
            raise HTTPException(status_code=405, detail="Admin user can not be deleted")
        # delete the book with the particular id, save the database and sending the response to the client.
        sess.delete(user)
        sess.commit()
        response = {"ok": True}
        return response




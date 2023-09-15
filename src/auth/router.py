from typing import List
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from .controllers.user import (
    change_email, register, get_user_by_name, get_users,
    delete_user, change_name,
)
from . import schemas
from database import get_db


router = APIRouter(
    prefix='/user',
    tags=['Auth']
)


@router.get('/all_users', response_model=List[schemas.User], status_code=201)
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db=db)


@router.get('/{id}', response_model=schemas.User, status_code=201)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_name(db=db, data=id)


@router.post('/create', response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)


@router.delete('/delete_user/{id}', status_code=201)
def user_del(id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, id=id)


@router.put('/change_name/{id}')
def new_name(id: int, new_name: str, db: Session = Depends(get_db)):
    return change_name(id=id, new_name=new_name, db=db)


@router.put('/chage_email/{id}')
def new_email(id: int, email: EmailStr, db: Session = Depends(get_db)):
    return change_email(id=id, email=email, db=db)

from typing import List
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from ..controllers.user import (
    change_email, register, get_user_by_name, get_users,
    delete_user, change_name
)
from .. import schemas
from database import get_db


router = APIRouter(
    prefix='/user',
    tags=['Auth']
)

@router.get('/all_users', response_model=List[schemas.UserFull], status_code=201)
async def get_all_users(db: Session = Depends(get_db)):
    return await get_users(db=db)


@router.get('/{username}', response_model=schemas.UserFull, status_code=201)
async def get_user(username: str, db: Session = Depends(get_db)):
    return await get_user_by_name(db=db, data=username)


@router.post('/create', response_model=schemas.User, status_code=201)
async def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return await register(db=db, user_data=user_data)


@router.delete('/delete_user/{id}', status_code=201)
async def user_del(id: int, db: Session = Depends(get_db)):
    return await delete_user(db=db, id=id)


@router.put('/change_name/{id}')
async def new_name(id: int, new_name: str, db: Session = Depends(get_db)):
    return await change_name(id=id, new_name=new_name, db=db)


@router.put('/chage_email/{id}')
async def new_email(id: int, new_email: EmailStr, db: Session = Depends(get_db)):
    return await change_email(id=id, email=new_email, db=db)

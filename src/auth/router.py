from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .controllers.user import register, get_user
from . import models, schemas
from database import get_db


router = APIRouter(
    prefix='/user',
    tags=['Auth']
)

@router.get('/all_users', response_model=schemas.UserLite)
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# Напиши вывод всех пользователей

@router.get('/{username}', response_model=schemas.UserLite, status_code=201)
def get_user_by_name(username: str, db: Session = Depends(get_db)):
    return get_user(db=db, data=username)

@router.post('/create', response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)
    
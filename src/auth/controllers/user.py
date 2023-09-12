from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from auth.models import User
from auth.schemas import UserCreate, UserLite
from ..secure.hp import pwd_context


def get_user(db: Session, data: str):
    user = db.query(User).filter(User.username == data).first()
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User does not exists"
        )
    
    return user

def register(db: Session, user_data: UserCreate):
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
    user = User(username=user_data.username,
                email=user_data.email,
                password=pwd_context.hash(user_data.password),
                role_id=3
                )
    db.add(user)
    db.commit()

    return user

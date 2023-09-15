from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy import or_

from auth.models import User, Role
from auth.schemas import UserCreate
from ..secure.hp import pwd_context


def meta_user(id: int, db: Session):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User is not found."
        )

    return user


def get_user_by_name(db: Session, data: str):
    user = db.query(User).filter(User.username == data).join(
        Role, Role.id == User.role_id).first()
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User does not exists"
        )

    return user


def get_users(db: Session):
    return db.query(User).all()

# Output all users


def register(db: Session, user_data: UserCreate):
    if db.query(User).filter(or_(
            User.email == user_data.email,
            User.username == user_data.username)).first():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User already exists."
        )

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=pwd_context.hash(user_data.password),
        role_id=3
    )
    db.add(user)
    db.commit()

    return user


def delete_user(db: Session, id: int):
    user = meta_user(db=db, id=id)
    db.delete(user)
    db.commit()

    return {
        "Status": {
            "OK": "User deleted",
        },
    }


def change_name(db: Session, id: int, new_name: str):
    user = meta_user(db=db, id=id)
    user.username = new_name
    db.commit()

    return {
        "Status": {
            "OK": "Username updated successfully",
        },
    }


def change_email(id: int, email: EmailStr, db: Session):
    user = meta_user(id=id, db=db)
    user.email = email
    db.commit()

    return {
        "Status": {
            "OK": "Email updated successfully",
        },
    }

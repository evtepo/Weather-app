from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_406_NOT_ACCEPTABLE
from sqlalchemy import or_

from auth.models import User, Role
from auth.schemas import UserCreate
from auth.secure.hp import get_hashed_password, verify_password
from auth.controllers.login import authentication


async def meta_user(username: str, db: Session):
    user = db.query(User, Role).join(Role).filter(User.username==username).first()
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User is not found."
        )
    
    role = user[1]
    user = user[0]
    user.role = role

    return user


# Basic user operations
async def get_users(db: Session):
    users = db.query(User, Role).join(Role).all()
    if users:
        for i in range(len(users)):
            user = users[i]
            role = user[1]
            user = user[0]
            user.role = role
            users[i] = user

    return users


async def get_user_by_name(username: str, db: Session):
    user = await meta_user(username=username, db=db)

    return user


async def register(user_data: UserCreate, db: Session):
    if db.query(User).filter(or_(
            User.email == user_data.email,
            User.username == user_data.username)).first():
        raise HTTPException(
            status_code=HTTP_406_NOT_ACCEPTABLE,
            detail="User already exists."
        )

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=get_hashed_password(user_data.password),
        role_id=3
    )
    db.add(user)
    db.commit()

    return user


async def delete_user(username: str, db: Session):
    user = await meta_user(username=username, db=db)
    db.delete(user)
    db.commit()

    return {
        "Status": {
            "OK": "User deleted.",
        },
    }
    

async def change_name(user: User, new_name: str, db: Session):
    if db.query(User).filter(User.username == new_name).first():
        raise HTTPException(
            status_code=HTTP_406_NOT_ACCEPTABLE,
            detail="This username is taken"
        )
    
    user.username = new_name
    db.commit()

    return {
        "Status": {
            "OK": "Username updated successfully.",
        },
    }


async def change_email(user: User, email: EmailStr, db: Session):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(
            status_code=HTTP_406_NOT_ACCEPTABLE,
            detail="This email is taken"
        )
    
    user.email = email
    db.commit()

    return {
        "Status": {
            "OK": "Email updated successfully.",
        },
    }


async def change_password(current_user: User, old_pass: str, new_password: str, db: Session):
    user = await authentication(username=current_user.username, password=old_pass, db=db)
    user.password = get_hashed_password(password=new_password)
    db.commit()

    return {
        "Status": {
            "OK": "Password updated successfully.",
        },
    }


async def change_user_role(username: str, role: int, db: Session):
    user = db.query(User).filter(User.username == username).first()
    user.role_id = role
    db.commit()

    return {
        "Status": {
            "OK": "User role updated successfully.",
        },
    }

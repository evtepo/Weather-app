from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette.status import HTTP_405_METHOD_NOT_ALLOWED

from auth.controllers.login import get_user_from_jwt

from auth import schemas
from auth import models
from database import get_db
from auth.controllers.user import (
    change_email, change_password, change_user_role, meta_user, register, get_user_by_name, get_users,
    delete_user, change_name
)

router = APIRouter(
    prefix='/user',
    tags=['Auth']
)


@router.get('/all_users', response_model=List[schemas.UserFull], status_code=201)
async def get_all_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    return await get_users(db=db)


@router.get('/{username}', response_model=schemas.UserFull, status_code=201)
async def get_user(username: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    return await get_user_by_name(username=username, db=db)


@router.post('/create', response_model=schemas.User, status_code=201)
async def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return await register(user_data=user_data, db=db)


@router.delete('/delete_user/{username}', status_code=201)
async def user_del(username: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    if current_user.role.name == "admin":
        return await delete_user(username=username, db=db)
    elif current_user.role.name == "moderator":
        deleted_user = await meta_user(username=username, db=db)
        if current_user.username == username or deleted_user.role.name == "member":
            return await delete_user(username=username, db=db)
    elif current_user.username == username and current_user.role.name == "member":
        return await delete_user(username=username, db=db)

    raise HTTPException(
        status_code=HTTP_405_METHOD_NOT_ALLOWED,
        detail="Action not available for this role"
    )


@router.put('/change_name/{username}')
async def new_name(new_name: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    return await change_name(user=current_user, new_name=new_name, db=db)


@router.put('/change_email/{username}')
async def new_email(new_email: EmailStr, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    return await change_email(user=current_user, email=new_email, db=db)


@router.put('/change_password/{old_password}')
async def new_pass(old_pass: str, new_pass: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    return await change_password(current_user=current_user, old_pass=old_pass, new_password=new_pass, db=db)


@router.put('change_role/{username}')
async def change_role(username: str, role: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    if current_user.role.name == "admin":
        if role in (2, 3):
            return await change_user_role(username=username, role=role, db=db)
        else:
            raise HTTPException(
                status_code=HTTP_405_METHOD_NOT_ALLOWED,
                detail="This role is not available"
            )

    raise HTTPException(
        status_code=HTTP_405_METHOD_NOT_ALLOWED,
        detail="Action not available for this role."
    )

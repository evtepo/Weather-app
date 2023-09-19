from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from datetime import timedelta

from database import get_db
from .user import get_user_by_name
from ..secure.token import create_access_token
from ..secure.hp import verify_password
from ..models import User

from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES, SECREY_KEY, ALGORITHM
)


# Getting token
async def authentication(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User is not found."
        )

    if not verify_password(password=password, hashed_password=user.password):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password."
        )

    return user


async def login_for_access_token(form_data: OAuth2PasswordRequestForm, db: Session):
    user = await authentication(username=form_data.username, password=form_data.password, db=db)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username,
        },
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


# Getting user by token
async def get_current_user_from_token(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    token_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={
            "Invalid token": "Could not validate credentials"
        }
    )
    try:
        payload = jwt.decode(token, SECREY_KEY, algorithms=ALGORITHM)
        username = payload.get("sub")
        if not username:
            raise token_exception
    except JWTError:
        raise token_exception

    user = await get_user_by_name(data=username, db=db)

    return user

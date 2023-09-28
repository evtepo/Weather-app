from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.controllers.login import login_for_access_token, get_user_from_jwt
from database import get_db
from auth import schemas, models


router = APIRouter(
    tags=['Login'],
    prefix='/login'
)


# Handler for getting token
@router.post('/token', response_model=schemas.Token)
async def access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login_for_access_token(form_data=form_data, db=db)


@router.get('/user', response_model=schemas.UserFull)
async def get_user_by_token(current_user: models.User = Depends(get_user_from_jwt)):
    return current_user

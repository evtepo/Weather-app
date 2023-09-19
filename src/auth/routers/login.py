from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..controllers.login import login_for_access_token, get_current_user_from_token
from database import get_db
from .. import schemas


router = APIRouter(
    tags=['Login'],
    prefix='/login'
)


# Handler for getting token
@router.post('/token', response_model=schemas.Token)
async def access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login_for_access_token(form_data=form_data, db=db)


@router.get('/test_token')
async def get_user_by_token(current_user: schemas.UserFull = Depends(get_current_user_from_token)):
    return {
        "Success": True,
        "current_user": current_user
    }

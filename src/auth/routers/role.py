from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.controllers.login import get_user_from_jwt
from auth.controllers.role import get_roles
from database import get_db
from auth import schemas, models

from fastapi_cache.decorator import cache


router = APIRouter(
    prefix='/role',
    tags=['Role']
)


@router.get('/all_roles', response_model=List[schemas.Role], status_code=201)
async def get_all_roles(db: Session = Depends(get_db), current_user: models.User = Depends(get_user_from_jwt)):
    if current_user.role.name in ("admin", "moderator"):
        return await get_roles(db=db)
    else:
        return {
            "Access denied": "Action not available for this role.",
        }

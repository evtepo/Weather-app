from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers.role import get_roles
from database import get_db
from auth import schemas


router = APIRouter(
    prefix='/role',
    tags=['Role']
)


@router.get('/all_roles', response_model=List[schemas.Role], status_code=201)
async def get_all_roles(db: Session = Depends(get_db)):
    return await get_roles(db=db)
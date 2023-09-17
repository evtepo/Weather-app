from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from auth.models import Role
from sqlalchemy.orm import Session


async def get_roles(db: Session):
    roles = db.query(Role).all()
    if not roles:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="No roles found"
        )

    return roles

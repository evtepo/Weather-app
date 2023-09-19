from datetime import timedelta, datetime
from typing import Optional
from jose import JWTError, jwt

from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES, SECREY_KEY, ALGORITHM
)

# Creation token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECREY_KEY, algorithm=ALGORITHM)

    return encode_jwt

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import redis

import os


load_dotenv()

# Database
DB_URL = os.environ.get('DB_URL')

# Token
SECREY_KEY = os.environ.get('JWT_SECREY_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

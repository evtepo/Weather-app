from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

import os


load_dotenv()

# Database
DB_URL = os.environ.get("DB_URL")

# Token
SECREY_KEY = os.environ.get("JWT_SECREY_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

# API keys from Yandex
YANDEX_WEATHER_API_KEY = os.environ.get("YANDEX_WEATHER_API_KEY")
YANDEX_GEOCODER_API_KEY = os.environ.get("YANDEX_GEOCODER_API_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/login")

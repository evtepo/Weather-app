from dotenv import load_dotenv

import os


load_dotenv()

# Database
DB_URL = os.environ.get('DB_URL')

# Token
SECREY_KEY = os.environ.get('JWT_SECREY_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_hashed_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    print(password, hashed_password)
    return pwd_context.verify(password, hashed_password) 

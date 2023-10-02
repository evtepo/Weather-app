from pydantic import BaseModel, EmailStr, Json


class Weather(BaseModel):
    Name: str
    Weather: dict


class Token(BaseModel):
    access_token: str
    token_type: str


class Role(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserFull(UserBase):
    id: int
    role: Role

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    role_id: int

    class Config:
        orm_mode = True

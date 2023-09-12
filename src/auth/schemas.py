from pydantic import BaseModel, EmailStr, Json


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLite(BaseModel):
    username: str
    role_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    role_id: int

    class Config:
        orm_mode = True


class Role(BaseModel):
    name: str
    permissions: Json

    class Config:
        orm_mode = True

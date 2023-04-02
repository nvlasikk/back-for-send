from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    firstName: str
    secondName: str
    surname: str
    email: str
    hashed_password: str
    job_title: str
    position: str
    phone: str
    photo: str
    is_admin: bool


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(User):
    pass


class UserUpdate(User):
    pass


class TokenBase:
    pass
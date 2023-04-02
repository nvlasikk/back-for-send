from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import parse_obj_as

from app.api.depends import get_db
from app.models.users import User
from app.schemas import users
from app.schemas.users import TokenBase, UserBase, UserCreate
from sqlalchemy.orm import Session

from app.service import user_service

router = APIRouter()


@router.post("/sing-up", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = user_service.get_user_by_email(db=db, email=user.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user_create=user)


@router.post("/login", response_model=UUID)
def auth(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: Optional[User] = user_service.get_user_by_email(db=db, email=form_data.username)

    if not user or user.hashed_password is not form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    token = user_service.create_user_token(db=db, user_id=user.id)
    return token
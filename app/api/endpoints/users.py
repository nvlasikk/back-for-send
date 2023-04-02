from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.users import User, UserCreate, UserUpdate
from app.service import user_service

router = APIRouter()


@router.get("/", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db=db)
    return users


@router.get("/{user_id}", response_model=Optional[User])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db=db, user_id=user_id)
    return user


@router.post("/", response_model=User)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user = user_service.create_user(user_create=user_create, db=db)
    return user


@router.put("/", response_model=User)
def update_user(user_update: UserUpdate, db: Session = Depends(get_db)):
    user = user_service.update_user(db=db, user_update=user_update)
    return user


@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.delete_user(db=db, user_id=user_id)
    return user

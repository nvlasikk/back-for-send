from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.user_crud import user_crud
from app.schemas.users import UserBase, User, UserCreate, UserUpdate


def get_all_users(db: Session) -> List[User]:
    user_db = user_crud.get_multi(db=db)
    return [User.from_orm(user) for user in user_db]


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    user_db = user_crud.get(db=db, id=user_id)
    if user_db is not None:
        return User.from_orm(user_db)
    else:
        return None


def create_user(db: Session, user_create: UserCreate) -> User:
    user_db = user_crud.create(db=db, obj_in=user_create)
    return User.from_orm(user_db)


def update_user(db: Session, user_update: UserUpdate) -> User:
    user_db = user_crud.get(db=db, id=user_update.id)
    user_create_db = user_crud.update(db=db, db_obj=user_db, obj_in=user_update)
    return User.from_orm(user_create_db)


def delete_user(db: Session, user_id: int) -> User:
    user_db = user_crud.remove(db=db, id=user_id)
    return User.from_orm(user_db)


def get_user_by_email(db: Session, email: str):
    return None


def create_user_token(db, user_id):
    return None
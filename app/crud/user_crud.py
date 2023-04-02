from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


user_crud = CRUDUser(User)

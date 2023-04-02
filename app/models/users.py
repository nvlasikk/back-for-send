from sqlalchemy import Column, Integer, String, Boolean

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    firstName = Column(String, nullable=False)
    secondName = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String(40), unique=True, index=True)
    hashed_password = Column(String)
    job_title = Column(String, nullable=False)
    position = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)

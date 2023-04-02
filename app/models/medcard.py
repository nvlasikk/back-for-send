from sqlalchemy import Column, Integer, String

from app.db import Base


class MedCard(Base):
    __tablename__ = "medcard"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    cardNumber = Column(Integer, nullable=False)
    firstName = Column(String, nullable=False)
    secondName = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    contacts = Column(String, nullable=False)
    address = Column(String, nullable=False)
    blood_group = Column(String, nullable=False)
    passportNumber = Column(String, nullable=False)

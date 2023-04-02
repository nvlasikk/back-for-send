from datetime import datetime

from pydantic import BaseModel


class MedCardBase(BaseModel):
    cardNumber: int
    firstName: str
    secondName: str
    surname: str
    gender: str
    contacts: str
    address: str
    blood_group: str
    passportNumber: str


class MedCard(MedCardBase):
    id: int

    class Config:
        orm_mode = True


class MedCardCreate(MedCardBase):
    pass


class MedCardUpdate(MedCard):
    pass

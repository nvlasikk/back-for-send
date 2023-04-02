from datetime import datetime

from pydantic import BaseModel


class AppointmentsBase(BaseModel):
    medcard_id: int
    user_id: int
    date: datetime
    time: str
    email: str


class Appointments(AppointmentsBase):
    id: int

    class Config:
        orm_mode = True


class AppointmentsCreate(AppointmentsBase):
    pass


class AppointmentsUpdate(Appointments):
    pass


class AppointmentsRequest(BaseModel):
    passportNumber: str
    email: str
    user_id: int
    date: datetime
    time: str

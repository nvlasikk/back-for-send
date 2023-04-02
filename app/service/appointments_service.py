from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.appointments_crud import appointments_crud
from app.schemas.appointments import Appointments, AppointmentsCreate


def get_all_appointments(db: Session) -> List[Appointments]:
    appointments_db = appointments_crud.get_multi(db=db)
    return [Appointments.from_orm(appointment) for appointment in appointments_db]


def get_appointment_by_id(db: Session, appointment_id: int) -> Optional[Appointments]:
    appointment_db = appointments_crud.get(db=db, id=appointment_id)
    return Appointments.from_orm(appointment_db)


def create_appointment(db: Session, appointment_create: AppointmentsCreate):
    appointment_db = appointments_crud.create(db=db, obj_in=appointment_create)
    return Appointments.from_orm(appointment_db)


def delete_appointment(db: Session, appointment_id: int):
    appointment_db = appointments_crud.remove(db=db, id=appointment_id)
    return Appointments.from_orm(appointment_db)

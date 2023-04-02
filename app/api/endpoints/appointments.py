from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.appointments import Appointments, AppointmentsCreate, AppointmentsUpdate, AppointmentsRequest
from app.service import appointments_service, medcard_service

router = APIRouter()


@router.get("/", response_model=List[Appointments])
def get_all_appointments(db: Session = Depends(get_db)):
    appointments = appointments_service.get_all_appointments(db=db)
    return appointments


@router.get("/{appointment_id}", response_model=Optional[Appointments])
def get_appointment_by_id(appointment_id: int, db: Session = Depends(get_db)):
    appointmetns = appointments_service.get_appointment_by_id(db=db, appointment_id=appointment_id)
    return appointmetns


@router.post("/", response_model=Appointments)
def create_appointment(appointment_request: AppointmentsRequest, db: Session = Depends(get_db)):
    medcard = medcard_service.get_medcard_by_passport_number(db=db, passportNumber=appointment_request.passportNumber)
    appointment_create = AppointmentsCreate(
        medcard_id=medcard.id,
        user_id=appointment_request.user_id,
        date=appointment_request.date,
        time=appointment_request.time,
        email=appointment_request.email
    )
    appointment = appointments_service.create_appointment(db=db, appointment_create=appointment_create)
    return appointment


@router.delete("/{appointment_id}", response_model=Appointments)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = appointments_service.delete_appointment(db=db, appointment_id=appointment_id)
    return appointment

from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Appointments
from app.schemas.appointments import AppointmentsCreate, AppointmentsUpdate


class CRUDAppointments(CRUDBase[Appointments, AppointmentsCreate, AppointmentsUpdate]):
    pass


appointments_crud = CRUDAppointments(Appointments)

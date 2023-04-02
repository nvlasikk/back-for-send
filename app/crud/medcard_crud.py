from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import MedCard
from app.schemas.medcard import MedCardCreate, MedCardUpdate


class CRUDMedCard(CRUDBase[MedCard, MedCardCreate, MedCardUpdate]):
    def get_by_passport_number(self, db: Session, passportNumber: str):
        medcard_db = db.query(self.model).filter(self.model.passportNumber == passportNumber).one_or_none()
        return medcard_db


medcard_crud = CRUDMedCard(MedCard)

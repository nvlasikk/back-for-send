from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.medcard_crud import medcard_crud
from app.schemas.medcard import MedCard, MedCardBase, MedCardCreate, MedCardUpdate


def get_all_medcard(db: Session) -> List[MedCard]:
    medcards_db = medcard_crud.get_multi(db=db)
    return [MedCard.from_orm(medCard) for medCard in medcards_db]


def get_medcard_by_id(db: Session, medcard_id: int) -> Optional[MedCard]:
    medcard_db = medcard_crud.get(db=db, id=medcard_id)
    return MedCard.from_orm(medcard_db)


def create_medcard(db: Session, medcard_create: MedCardCreate) -> MedCard:
    medcard_db = medcard_crud.create(db=db, obj_in=medcard_create)
    return MedCard.from_orm(medcard_db)


def update_medcard(db: Session, medcard_update: MedCardUpdate) -> MedCard:
    medcard_db = medcard_crud.get(db=db, id=medcard_update.id)
    medcard_update_db = medcard_crud.update(db=db, db_obj=medcard_db, obj_in=medcard_update)
    return MedCard.from_orm(medcard_update_db)


def delete_medcard(db: Session, medcard_id: int) -> MedCard:
    medcard_db = medcard_crud.remove(db=db, id=medcard_id)
    return MedCard.from_orm(medcard_db)


def get_medcard_by_passport_number(db: Session, passportNumber: str):
    medcard_db = medcard_crud.get_by_passport_number(db=db, passportNumber=passportNumber)
    return MedCard.from_orm(medcard_db)

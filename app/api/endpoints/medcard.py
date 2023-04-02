from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.medcard import MedCard, MedCardBase, MedCardUpdate, MedCardCreate
from app.service import medcard_service

router = APIRouter()


@router.get("/", response_model=List[MedCard])
def get_all_medcard(db: Session = Depends(get_db)):
    medcard = medcard_service.get_all_medcard(db=db)
    return medcard


@router.get("/{medcard_id}", response_model=Optional[MedCard])
def get_medcard_by_id(medcard_id: int, db: Session = Depends(get_db)):
    medcard = medcard_service.get_medcard_by_id(db=db, medcard_id=medcard_id)
    return medcard


@router.post("/", response_model=MedCard)
def create_medcard(medcard_create: MedCardCreate, db: Session = Depends(get_db)):
    medcard = medcard_service.create_medcard(db=db, medcard_create=medcard_create)
    return medcard


@router.put("/", response_model=MedCard)
def update_medcard(medcard_update: MedCardUpdate, db: Session = Depends(get_db)):
    medcard = medcard_service.update_medcard(db=db, medcard_update=medcard_update)
    return medcard


@router.delete("/{medcard_id}", response_model=MedCard)
def delete_medcard(medcard_id: int, db: Session = Depends(get_db)):
    medcard = medcard_service.delete_medcard(db=db, medcard_id=medcard_id)
    return medcard

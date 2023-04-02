from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.service import Service, ServiceBase, ServiceUpdate, ServiceCreate
from app.service import services_service

router = APIRouter()


@router.get("/", response_model=List[Service])
def get_all_services(db: Session = Depends(get_db)):
    services = services_service.get_all_services(db=db)
    return services

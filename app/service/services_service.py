from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.service_crud import service_crud
from app.schemas.service import Service, ServiceBase, ServiceUpdate, ServiceCreate


def get_all_services(db: Session) -> List[Service]:
    services_db = service_crud.get_multi(db=db)
    return [Service.from_orm(service) for service in services_db]

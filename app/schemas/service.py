from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    costService: int
    costCosumable: int


class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(Service):
    pass

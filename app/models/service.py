from sqlalchemy import Column, Integer, String, Boolean

from app.db import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, nullable=False)
    costService = Column(Integer, nullable=False)
    costCosumable = Column(Integer, nullable=False)

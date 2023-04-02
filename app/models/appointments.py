from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Time
from sqlalchemy.orm import relationship

from app.db import Base
from app.models.medcard import MedCard
from app.models.users import User


class Appointments(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String(40), unique=True, index=True)
    medcard_id = Column(Integer, ForeignKey("medcard.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, nullable=False)
    time = Column(String, nullable=False)

    medcard = relationship('MedCard', foreign_keys=[medcard_id],
                           primaryjoin='MedCard.id == Appointments.medcard_id')


from fastapi import APIRouter

from app.api.endpoints import users, medcard, appointments, service

api_routers = APIRouter()
api_routers.include_router(users.router, prefix="/users", tags=["User"])
api_routers.include_router(medcard.router, prefix="/medcard", tags=["MedCard"])
api_routers.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
api_routers.include_router(service.router, prefix="/service", tags=["Service"])

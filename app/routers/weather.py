from fastapi import APIRouter
from app.services.weather_service import get_weather

router = APIRouter(
    prefix="/weather",
    tags=["weather"]
)

@router.get("/latest")
def latest(city: str = "tokyo"):
    return get_weather(city)
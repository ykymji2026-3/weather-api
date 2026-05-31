from fastapi import FastAPI
from app.routers import weather
from app.db.database import engine
from app.models.weather_record import WeatherRecord

WeatherRecord.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(weather.router)

@app.get("/")
def root():
    return {
        "message": "weather api is running"
    }
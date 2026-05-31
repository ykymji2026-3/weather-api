from sqlalchemy import Column, Integer, String, Float

from app.db.database import Base

class WeatherRecord(Base):

    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)

    city = Column(String)

    temperature = Column(Float)

    windspeed = Column(Float)

    weather_code = Column(Integer)
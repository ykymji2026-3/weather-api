import requests

CITY_COORDS = {
    "tokyo": {
        "latitude": 35.6895,
        "longitude": 139.6917
    },
    "osaka": {
        "latitude": 34.6937,
        "longitude": 135.5023
    }
}

def get_weather(city: str):

    city = city.lower()

    if city not in CITY_COORDS:
        return {
            "error": "unsupported city"
        }

    coords = CITY_COORDS[city]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "current_weather": True
    }

    response = requests.get(url, params=params)

    data = response.json()

    current = data["current_weather"]

    return {
        "city": city,
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weather_code": current["weathercode"]
    }
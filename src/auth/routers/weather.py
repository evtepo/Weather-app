from fastapi import APIRouter, Depends

from auth import models
from auth.controllers.login import get_user_from_jwt
from api.api import get_weather, get_cords
from auth.schemas import Weather


router = APIRouter(
    tags=["Weather"]
)

@router.get('/{city}', response_model=Weather, status_code=201)
async def get_weather_by_city(city: str, current_user: models.User = Depends(get_user_from_jwt)):
    data = await get_cords(city)
    name, longitude, latitude = data.get("Name"), *data.get("Cords").split()
    weather = await get_weather(latitude, longitude)

    return {
        "Name": name, 
        "Weather": weather
    }

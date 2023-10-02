import requests

import json

from config import YANDEX_WEATHER_API_KEY, YANDEX_GEOCODER_API_KEY


async def get_cords(city: str):
    request = requests.get(
        url=f"https://geocode-maps.yandex.ru/1.x/?apikey={YANDEX_GEOCODER_API_KEY}&geocode={city}&format=json",
    )
    items = json.loads(request.text)
    result = {}

    name = items["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
    cords = items["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

    result.update({
        "Name": name,
        "Cords": cords
    })
    
    return result


async def get_weather(latitude: float, longitude: float):
    request = requests.get(
        url=f"https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}",
        headers={
            "X-Yandex-API-Key": YANDEX_WEATHER_API_KEY,
        },
    )

    items = json.loads(request.text)
    season = items.get("fact").get("season")
    date = items.get("forecasts")[0].get("date")
    temp = items.get("fact").get("temp")
    feels_like = items.get("fact").get("feels_like")
    condition = items.get("fact").get("condition")
    wind_speed = items.get("fact").get("wind_speed")
    sunrice = items.get("forecasts")[0].get("sunrise")
    sunset = items.get("forecasts")[0].get("sunset")

    data = {
        "Season": season.capitalize(),
        "Date": date,
        "Temp": temp,
        "Feels like": feels_like,
        "Condition": condition.capitalize(),
        "Wind speed": wind_speed,
        "Sunrice": sunrice.capitalize(),
        "Sunset": sunset.capitalize(),
    }

    return data

from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from auth.routers.user import router as auth_router
from auth.routers.role import router as role_router
from auth.routers.login import router as login_router
from auth.routers.weather import router as weather_router

from config import REDIS_HOST, REDIS_PORT


app = FastAPI(
    title='Weather',
)

app.include_router(
    router=auth_router
)

app.include_router(
    router=role_router
)

app.include_router(
    router=login_router
)

app.include_router(
    router=weather_router
)


@app.on_event("startup")
async def stertup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

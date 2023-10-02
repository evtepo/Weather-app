from fastapi import FastAPI
from auth.routers.user import router as auth_router
from auth.routers.role import router as role_router
from auth.routers.login import router as login_router
from auth.routers.weather import router as weather_router


app = FastAPI(
    title='Weather'
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

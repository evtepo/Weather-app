from fastapi import FastAPI
from auth.router import router as auth_router


app = FastAPI(
    title='Weather'
)

app.include_router(
    router=auth_router
)

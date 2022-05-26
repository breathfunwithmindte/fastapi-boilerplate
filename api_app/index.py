from fastapi import FastAPI

from fastapi import FastAPI
from api_app.routes.Users import users_router

api_app = FastAPI()

api_app.include_router(users_router)

@api_app.get("/")
async def root():
    return "hello world from api_  just_app"
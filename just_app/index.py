from fastapi import FastAPI
from just_app.routes.TestingResponse import testing_router

just_app = FastAPI()

just_app.include_router(testing_router);


@just_app.get("/")
async def root():
    return "hello world from just just_app"
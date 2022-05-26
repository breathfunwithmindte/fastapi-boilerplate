from fastapi import FastAPI
from just_app.index import just_app
from api_app.index import api_app

app = FastAPI()

app.mount("/just-app/", just_app)
app.mount("/api/v1/", api_app)


@app.get("/")
async def root():
    return "hello world from just_app"

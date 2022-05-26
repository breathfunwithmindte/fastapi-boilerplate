from fastapi import APIRouter, Request, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
import json

from api_app.data_models.users.UserFormstate import UserFormstate

users_router = APIRouter()


@users_router.get("/users/list")
async def res_users(limit: int = 3):
    print("users api limit is = ", limit)
    return [{"username": "Mike"}, {"username": "Ricky"}]

@users_router.get("/users/{id}")
async def res_users(id: str):
    return {"username": "Nancy", "id": id}

@users_router.post("/users/new")
async def newuser (UserFormstate: UserFormstate):

    return { "user": UserFormstate }

@users_router.post("/users/new/test-file")
async def usernew_withfile(request: Request, file: UploadFile, file1: bytes = File()):
    data = await file.read();
    file = open("storage/hello.jpeg", "wb")
    file.write(data)
    file.close()
    print(len(data))
    return {"file_size": "Asdasd"}

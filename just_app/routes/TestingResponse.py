from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, Response, PlainTextResponse, StreamingResponse, FileResponse, JSONResponse
import json


testing_router = APIRouter()


@testing_router.get("/normal")
async def res_normal():
    return [{"username": "Mike"}, {"username": "Ricky"}]

@testing_router.get("/json")
async def res_normal():
    return JSONResponse(status_code=202, content={"hi": "hi from json type response"})

@testing_router.get("/json-encode")
async def res_normal():
    nana = { "hi": "hi from json encode" }
    return Response(status_code=202, content=json.dumps(nana), media_type="application/json")

@testing_router.get("/file-response")
async def res_normal():
    return FileResponse("just_app/routes/testing.txt")



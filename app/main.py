"""Main module for test fastapi"""

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()


class SNums(BaseModel):
    num1: int
    num2: int


@app.get("/")
async def root():
    """Index root page"""
    return FileResponse("app/templates/index.html")


@app.post("/calculate")
async def calculate(body: SNums):
    """Endpoint for sum two numbers"""
    result = body.num1 + body.num2
    return JSONResponse({"result": result})

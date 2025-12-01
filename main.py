import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import scrape

app = FastAPI()

class wiki(BaseModel):
    name: str

@app.post("/wiki-summary")
async def wiki_summary(item: wiki):
    result = scrape(item.name, length=3)
    payload = {"summary": result}
    json_Compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_Compatible_item_data)

@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Functions"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Addition of two numbers with GET HTTP Method"""
    total = num1 + num2
    return {"total": total}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")
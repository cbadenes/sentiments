from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class Msg(BaseModel):
    inputs: str

specific_model = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/sentiments")
async def create_sentiment_post(inp:Msg):
    print("received:",inp)
    result = specific_model([inp.inputs])
    return result
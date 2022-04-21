from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests

from call_yelp_api import FoodRequest


class FoodQuiz(BaseModel):
    food: str
    distance: str
    location: str
    price: str


app = FastAPI()


@app.get("/restaurants")
def read_root():
    food = FoodRequest("Chinese", "1", "Boston", "1")
    return food.post_data()


@app.post("/quiz-form")
async def read_food(foodQuiz: FoodQuiz):
    food = FoodRequest(foodQuiz.food, foodQuiz.distance, foodQuiz.location, foodQuiz.price)
    return food.post_data()


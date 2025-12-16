import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from common.preprocessing import predict_yield

app = FastAPI()

class Input(BaseModel):
    region: str
    soil: str
    crop: str
    weather: str
    rainfall: float
    temperature: float
    fertilizer: bool
    irrigation: bool
    days: int

@app.post("/predict")
def predict(data: Input):
    predicted_yield = predict_yield(
        data.region, data.soil, data.crop, data.weather,
        data.rainfall, data.temperature,
        data.fertilizer, data.irrigation, data.days
    )
    return {"yield": predicted_yield}

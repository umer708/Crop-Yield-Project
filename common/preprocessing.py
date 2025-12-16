import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "../model/best_crop_yield_model.pkl"))
encodings = joblib.load(os.path.join(BASE_DIR, "../model/encoding_maps.pkl"))

def prepare_input(region, soil, crop, weather, rainfall, temperature, fertilizer, irrigation, days):
    return np.array([[
        encodings['Region'][region],
        encodings['Soil_Type'][soil],
        encodings['Crop'][crop],
        rainfall,
        temperature,
        int(fertilizer),
        int(irrigation),
        encodings['Weather_Condition'][weather],
        days
    ]])

def predict_yield(*args):
    X = prepare_input(*args)
    return model.predict(X)[0]

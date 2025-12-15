from fastapi import FastAPI
import joblib

from .schemas import HouseInput

model = joblib.load("../models/house_model.pkl")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "House Price Prediction API is running"}

@app.host("/predict")
def predict_price(data : HouseInput):
    features = [[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]]

    prediction = model.predict(features)
    return {"predicted_price": float(prediction[0])}
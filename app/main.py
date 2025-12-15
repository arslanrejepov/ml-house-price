from fastapi import FastAPI
import joblib
from pathlib import Path

from .schemas import HouseInput

app = FastAPI()

# ===============================
# Load model using absolute path
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "house_model.pkl"

model = joblib.load(MODEL_PATH)


# ===============================
# Test endpoint
# ===============================
@app.get("/")
def root():
    return {"message": "House Price Prediction API is running"}


# ===============================
# Prediction endpoint
# ===============================
@app.post("/predict")
def predict_price(data: HouseInput):
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

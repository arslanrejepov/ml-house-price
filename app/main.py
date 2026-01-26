import os
import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .schemas import HouseInput

app = FastAPI()

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")

# --- STATIC ---
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- LOAD MODEL ONCE ---
model = joblib.load(MODEL_PATH)

@app.get("/")
async def index():
    return FileResponse(INDEX_HTML)

@app.post("/predict")
async def predict(data: HouseInput):
    features = np.array([[
        data.MedInc,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]])

    prediction = model.predict(features)[0]

    return {
        "prediction": float(prediction),
        "prediction_text": f"${prediction * 100000:,.2f}",
        "status": "success"
    }

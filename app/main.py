import os
import random
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .schemas import HouseInput

app = FastAPI()

# --- CRITICAL FIX: PATH SETUP ---
# We get the folder where THIS file (main.py) is located (the 'app' folder)
current_dir = os.path.dirname(os.path.abspath(__file__))

# We tell Python that 'static' and 'index.html' are right here in the same folder
static_dir = os.path.join(current_dir, "static")
index_path = os.path.join(current_dir, "index.html")

# Mount the static folder so the HTML can see CSS and images
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# --- ROUTES ---

@app.get("/")
async def read_index():
    return FileResponse(index_path)

@app.post("/predict")
async def predict_house(data: HouseInput):
    # Fake prediction logic for testing
    fake_price = (data.MedInc * 40000) + (data.AveRooms * 5000) + random.randint(-5000, 5000)
    
    return {
        "prediction_text": f"${fake_price:,.2f}", 
        "raw_value": fake_price,
        "status": "success"
    }
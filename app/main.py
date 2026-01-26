import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 1. Get the current folder where this main.py file lives
base_dir = os.path.dirname(__file__)

# 2. Tell the code that 'static' and 'index.html' are right here next to main.py
static_dir = os.path.join(base_dir, "static")
index_path = os.path.join(base_dir, "index.html")

# 3. Mount the static directory using the absolute path
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_index():
    # 4. Serve the index.html using the absolute path
    return FileResponse(index_path)

# ... (Keep your existing prediction endpoint code below here)
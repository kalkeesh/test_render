from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="MongoDB Render Test")

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["chat_db"]  # Change if needed
collection = db["messages"]

@app.get("/", response_class=HTMLResponse)
async def read_data():
    data = await collection.find_one()
    if not data:
        return HTMLResponse("<h2>No data found in collection.</h2>")
    html_content = f"<h2>Data from MongoDB:</h2><pre>{data}</pre>"
    return HTMLResponse(content=html_content)

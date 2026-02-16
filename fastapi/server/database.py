from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Optimized Mongo Client
client = AsyncIOMotorClient(
    MONGO_URL,
    maxPoolSize=50,          # connection pool
    minPoolSize=5,
    serverSelectionTimeoutMS=5000,
)

db = client[DATABASE_NAME]

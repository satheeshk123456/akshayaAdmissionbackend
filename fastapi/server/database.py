from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
# get values from env
MONGO_URL = os.getenv("MONGO_URL")
PORT = os.getenv("PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# mongo connetion
client  = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

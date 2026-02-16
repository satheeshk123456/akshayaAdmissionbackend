# controllers/common_controller.py
from ..database import db

async def get_user_data(targettable: str, userEmail: str):
    collection = db[targettable]

    cursor = collection.find({"email": userEmail})
    result = []

    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        result.append(doc)

    return result

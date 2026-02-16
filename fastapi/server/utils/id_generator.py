from ..database import db
from pymongo import ReturnDocument


async def get_next_sequence(name: str):

    document = await db["admissioncounter"].find_one_and_update(
        {"_id": name},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )

    return document["sequence_value"]

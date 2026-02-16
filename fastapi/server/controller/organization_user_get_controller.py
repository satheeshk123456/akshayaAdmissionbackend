from ..database import db
async def getorgani():
    collection=db["organization"]
    data=[]
    async for doc in collection.find({}):
        doc["_id"]=str(doc["_id"])
        data.append(doc)
    return data

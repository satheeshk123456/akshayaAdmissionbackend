from ..database import db
from ..model.allform_model import Allform

async def save_all_form(data:Allform):
    collection=db["AllFormUser"+data.userRoleLabel]
    result=await collection.insert_one(data.dict())


    return str(result.inserted_id)

async def get_all_form_data(userrole_get, userEmail):
    collection1 = db["AllFormUser" + userrole_get]
    result1 = await collection1.find_one({"email": userEmail})

    if not result1:
        return None

    # Convert ObjectId to string
    result1["_id"] = str(result1["_id"])
    return result1


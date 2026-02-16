from fastapi import HTTPException
from ..database import db

async def forgetpasscontroller(userdata: dict):
    email = userdata.email
    password = userdata.password
    user_type = userdata.userType

    if not email or not password or not user_type:
        raise HTTPException(status_code=400, detail="Missing required fields")

    # Select the correct collection based on userType
    if user_type.lower() == "individual":
        collection = db["individual"]
    elif user_type.lower() == "organization":
        collection = db["organization"]
    else:
        raise HTTPException(status_code=400, detail="Invalid userType")

    # Find the user by email
    user = await collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update password as plain text
    await collection.update_one({"email": email}, {"$set": {"password": password}})

    return {"message": "Password updated successfully"}

from fastapi import HTTPException
from ..database import db
from ..model.userregister_model import User

async def create_user(user_data: User):
    collection = db[user_data.targetTable]  # dynamic table

    # Check only email (correct)
    existing_user = await collection.find_one({"email": user_data.email})
    print("Existing user:", existing_user)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists with this email"
        )

    # Check BOTH email + role (optional)
    existing_role_user = await collection.find_one({
        "email": user_data.email,
        "userRoleValue": user_data.userRoleValue
    })
    if existing_role_user:
        raise HTTPException(
            status_code=400,
            detail="User with this role already exists"
        )
    user_dic=user_data.dict()
    user_dic["status"]="pending"
    # Save user
    result = await collection.insert_one(user_dic)

    return {
        "message": "User registered successfully",
        "userId": str(result.inserted_id)
    }

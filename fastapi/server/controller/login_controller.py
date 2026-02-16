# from ..database import db
# from fastapi import HTTPException
# # 
# async def login_user_controller(data):
#     # Print incoming request data
#     print("Login Attempt:")
#     print("Account Type:", data.accountType)
#     print("Email:", data.email)
#     print("Password:", data.password)

#     email = data.email
#     password = data.password
#     accountType = data.accountType  # should be "individuals" / "organizations"

#     collection = db[accountType]

#     user = await collection.find_one({"email": email})
#     print(user)
#     if not user:
#         print(f"Login Failed: User not found in {accountType} for email {email}")
#         raise HTTPException(status_code=400, detail="User not found")

#     if user["password"] != password:
#         print(f"Login Failed: Wrong password for email {email} in {accountType}")
#         raise HTTPException(status_code=400, detail="Wrong password")

#     print(f"Login Successful for email {email} in {accountType}")
#     return {
#         "message": "Login successful",
#         "userId": str(user["_id"]),
#         "accountType": accountType,
#         "userRoleLabel":str(user["userRoleLabel"])
        
#     }
from ..database import db
from fastapi import HTTPException
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta

# Load .env variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# Helper function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Login controller
async def login_user_controller(data):
    # Print incoming request data
    print("Login Attempt:")
    print("Account Type:", data.accountType)
    print("Email:", data.email)
    print("Password:", data.password)

    email = data.email
    password = data.password
    accountType = data.accountType  # should be "individuals" / "organizations"

    collection = db[accountType]

    user = await collection.find_one({"email": email})
    print(user)
    if not user:
        print(f"Login Failed: User not found in {accountType} for email {email}")
        raise HTTPException(status_code=400, detail="User not found")

    if user["password"] != password:
        print(f"Login Failed: Wrong password for email {email} in {accountType}")
        raise HTTPException(status_code=400, detail="Wrong password")

    print(f"Login Successful for email {email} in {accountType}")

    # ---------------- JWT Part ----------------
    token_data = {
        "userId": str(user["_id"]),
        "email": email,
        "role": str(user["userRoleLabel"]),
        "accountType": accountType
    }
    token = create_access_token(token_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # -----------------------------------------

    return {
        "message": "Login successful",
        "userId": str(user["_id"]),
        "accountType": accountType,
        "userRoleLabel": str(user["userRoleLabel"]),
        "token": token,
    }

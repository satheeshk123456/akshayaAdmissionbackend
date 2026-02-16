from fastapi import APIRouter
from ..model.email_model import EmailModel
from ..controller.email_controller import send_verification_email
from ..database import db
import uuid

router = APIRouter(prefix="/users")


# ---------------------------------------------------
# SEND VERIFICATION EMAIL
# ---------------------------------------------------
@router.post("/send-verification")
async def send_verification(data: EmailModel):

    token = str(uuid.uuid4())  # random verification token

    # Check if email exists in DB
    user = await db.users.find_one({"email": data.email})

    if user:
        # update token
        await db.users.update_one(
            {"email": data.email},
            {"$set": {"verify_token": token, "verified": False}}
        )
    else:
        # insert as new record
        await db.users.insert_one({
            "email": data.email,
            "verified": False,
            "verify_token": token
        })

    send_verification_email(data.email, token)

    return {"message": "Verification email sent"}


# ---------------------------------------------------
# VERIFY WHEN USER CLICKS LINK
# ---------------------------------------------------
@router.get("/verify")
async def verify_email(token: str):

    user = await db.users.find_one({"verify_token": token})

    if not user:
        return {"verified": False, "message": "Invalid or expired token"}

    await db.users.update_one(
        {"verify_token": token},
        {"$set": {"verified": True}, "$unset": {"verify_token": ""}}
    )

    return {"verified": True, "message": "Email verified successfully!"}


# ---------------------------------------------------
# CHECK VERIFICATION STATUS
# ---------------------------------------------------
@router.get("/check-verification")
async def check_status(email: str):

    user = await db.users.find_one({"email": email})

    if not user:
        return {"verified": False}

    return {"verified": user.get("verified", False)}

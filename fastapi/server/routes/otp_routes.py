from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from server.controller.otp_controller import generate_otp, check_otp

router = APIRouter(prefix="/users")

class SendOTPRequest(BaseModel):
    email: EmailStr
   

class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str

@router.post("/send-otp")
async def send_otp(req: SendOTPRequest):
    try:
        otp = generate_otp(req.email)
        return {"message": "OTP sent successfully", "otp": otp}  # you can remove "otp" in prod
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send OTP: {str(e)}")

@router.post("/verify-otp")
async def verify_otp_endpoint(req: VerifyOTPRequest):
    if check_otp(req.email, req.otp):
        return {"verified": True}
    return {"verified": False}

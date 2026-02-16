from datetime import datetime, timedelta

# Temporary in-memory OTP store
otp_store = {}  # {email: {"otp": "123456", "expires": datetime}}

def save_otp(email: str, otp: str, validity_minutes: int = 5):
    
    otp_store[email] = {
        "otp": otp,
        "expires": datetime.utcnow() + timedelta(minutes=validity_minutes)
    }

def verify_otp(email: str, otp: str) -> bool:
    data = otp_store.get(email)
    if not data:
        return False
    if data["otp"] != otp:
        return False
    if datetime.utcnow() > data["expires"]:
        del otp_store[email]
        return False
    del otp_store[email]  # remove OTP after successful verification
    return True

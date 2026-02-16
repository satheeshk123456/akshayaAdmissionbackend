from server.model.otp_model import save_otp, verify_otp
from server.utils.email_utils import send_email

def generate_otp(email: str) -> str:
    from random import randint
    otp = f"{randint(100000, 999999)}"
    save_otp(email, otp)
    send_email(
        email,
        "Your OTP Code",
        f"Your 6-digit OTP is: {otp}. It is valid for 5 minutes."
    )
    return otp

def check_otp(email: str, otp: str) -> bool:
    return verify_otp(email, otp)

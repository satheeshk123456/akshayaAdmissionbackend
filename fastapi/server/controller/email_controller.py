import smtplib
from email.mime.text import MIMEText

SMTP_EMAIL = "akshyathulir@gmail.com"
SMTP_PASSWORD = "vsir plyj bunf zyem"  # Use Gmail App Password

PROJECT_NAME = "Akshyathulir"


def send_verification_email(to_email, token):
    verify_link = f"http://localhost:8000/email/verify?token={token}"

    body = f"""
Hi,

Please verify your email for **{PROJECT_NAME}**.

Click the link below to verify your account:

{verify_link}

Thank you,
{PROJECT_NAME} Team
"""

    msg = MIMEText(body)
    msg["Subject"] = f"{PROJECT_NAME} - Email Verification"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)

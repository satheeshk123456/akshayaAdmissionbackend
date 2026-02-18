from ..database import db
from ..model.admission_model import AdmissionModel
from server.utils.email_utils import send_email
from server.utils.id_generator import get_next_sequence
from datetime import datetime
from fastapi import HTTPException, BackgroundTasks

async def admissionstore(data: AdmissionModel, background_tasks: BackgroundTasks):
    collection = db["admission_details"]
    admission_data = data.model_dump()

    email = admission_data.get("email")
    mobile = admission_data.get("mobile")

    # 1. Check for duplicate user
    existing_user = await collection.find_one({
        "$or": [
            {"email": email},
            {"mobile": mobile}
        ]
    })

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email or mobile number already exists"
        )

    # 2. Generate Unique Application ID
    sequence_number = await get_next_sequence("admission_id")
    year = datetime.utcnow().year
    unique_id = f"{year}akshaya{sequence_number}"

    admission_data["application_id"] = unique_id
    admission_data["status"] = "Admission Submitted"
    admission_data["submittedAt"] = datetime.utcnow()

    # 3. Save to MongoDB
    await collection.insert_one(admission_data)

    # 4. Trigger Email if email exists
    if email:
        email_body = f"""
{admission_data.get("college")}
-----------------------------------------

Dear {admission_data.get("fullname")},

Your admission application has been successfully submitted.

Application ID : {unique_id}

-----------------------------------------
Full Name        : {admission_data.get("fullname")}
Phone Number     : {admission_data.get("mobile")}
Email Address    : {admission_data.get("email")}
Date of Birth    : {admission_data.get("dob")}
State            : {admission_data.get("state")}
City             : {admission_data.get("city")}
School Name      : {admission_data.get("schoolSearch")}
Course Applied   : {admission_data.get("selectedCourse")}
-----------------------------------------

Our admissions team will review your application and contact you shortly.

Thank you for choosing Akshaya College.
"""

        # Non-blocking background task
        background_tasks.add_task(
            send_email,
            to_email=email,
            subject="Admission Submitted Successfully",
            body=email_body
        )

    return {
        "status": "success",
        "application_id": unique_id
    }
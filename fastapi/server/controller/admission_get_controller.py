from ..database import db
from bson import ObjectId

def serialize_admission(admission) -> dict:
   return {
    "id": str(admission.get("_id")),
    "category": admission.get("category"),
    "fullname": admission.get("fullname"),
    "email": admission.get("email"),
    "dob": admission.get("dob"),
    "mobile": admission.get("mobile"),
    "state": admission.get("state"),
    "city": admission.get("city"),
    "schoolType": admission.get("schoolType"),
    "schoolSearch": admission.get("schoolSearch"),
    "institution": admission.get("institution"),
    "college": admission.get("college"),
    "selectedCourse": admission.get("selectedCourse"),
    "status": admission.get("status"),
    "submittedAt": admission.get("submittedAt"),
}


async def get_all_admissions():
    admission_collection=db["admission_details"]
    cursor = admission_collection.find()

    # ✅ Convert Motor cursor to list
    admissions = await cursor.to_list(length=None)

    return [serialize_admission(adm) for adm in admissions]

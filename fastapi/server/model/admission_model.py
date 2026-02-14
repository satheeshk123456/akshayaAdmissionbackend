from pydantic import BaseModel, EmailStr
from typing import Optional

class AdmissionModel(BaseModel):
    category: str
    fullname: str
    email: EmailStr
    dob: str
    mobile: str
    state: str
    city: str
    schoolType: str
    schoolSearch: str
    institution: str
    college: str
    selectedCourse: str
    status: str
    submittedAt: str

from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    accountType: str           # individuals / organizations
    targetTable: str           # "individuals" or "organizations"
    userRoleValue: str
    userRoleLabel: str
    firstName: str
    lastName: str
    email: EmailStr
    mobile: str
    password: str
    registeredAt: Optional[str]
    user_id:str
    


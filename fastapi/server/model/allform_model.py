from  pydantic  import BaseModel

class Allform(BaseModel):
    firstName:str
    lastName:str
    userRoleLabel: str
    email:str


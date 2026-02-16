from pydantic import BaseModel

class Forgetpassmodel(BaseModel):
    email:str
    password:str
    userType:str

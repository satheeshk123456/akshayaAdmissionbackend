from pydantic import BaseModel

class ContactForm(BaseModel):
    name: str
    email: str
    phone: str
    inquiry: str
    message: str
    termsAgreed: bool

from ..database import db
from ..model.contact_model import ContactForm

async def save_contact_form(data: ContactForm):
    print("data",data)
    collection = db["contact_us"]  
     # collection name in MongoDB
    result = await collection.insert_one(data.dict())
   
    return str(result.inserted_id)

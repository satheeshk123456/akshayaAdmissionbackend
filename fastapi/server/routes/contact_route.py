from fastapi import APIRouter, HTTPException
from ..model.contact_model import ContactForm
from ..controller.contact_controller import save_contact_form

router = APIRouter(prefix="/contact", tags=["contact"])

@router.post("/submit")
async def submit_contact(form: ContactForm):
    try:
        inserted_id = await save_contact_form(form)
        return {"message": "Form submitted successfully", "id": inserted_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

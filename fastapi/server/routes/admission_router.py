from fastapi import APIRouter, HTTPException
from ..model.admission_model import AdmissionModel
from ..controller.admission_controller import admissionstore
router = APIRouter(prefix="/submit",tags=["admission"])
@router.post("/admissionpost")
async def admissionpost(data:AdmissionModel):
    return await admissionstore(data)
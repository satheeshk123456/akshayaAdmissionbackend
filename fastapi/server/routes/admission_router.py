from fastapi import APIRouter, HTTPException, BackgroundTasks
from ..model.admission_model import AdmissionModel
from ..controller.admission_controller import admissionstore

router = APIRouter(prefix="/submit", tags=["admission"])

@router.post("/admissionpost")
async def admissionpost(data: AdmissionModel, background_tasks: BackgroundTasks):
    return await admissionstore(data, background_tasks)

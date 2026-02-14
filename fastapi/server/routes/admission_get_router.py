from fastapi import APIRouter
from ..controller.admission_get_controller import get_all_admissions

router = APIRouter(prefix="/get" , tags=["admission"])

@router.get("/admissionsget")
async def fetch_admissions():
    return await get_all_admissions()

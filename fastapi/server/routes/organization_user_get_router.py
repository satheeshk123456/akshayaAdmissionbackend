from fastapi import APIRouter
from ..controller.organization_user_get_controller import getorgani

router=APIRouter(prefix="/getorganizationuser",tags=["users"])

@router.get("/getorganization")
async def getorgani_user():
    return await getorgani()
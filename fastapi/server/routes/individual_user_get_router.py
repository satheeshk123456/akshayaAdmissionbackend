from fastapi import APIRouter
from ..controller.individual_user_get_controller import getindivi

router=APIRouter(prefix="/getindividualusers",tags=["users"])

@router.get("/getindividual")
async def getindividualuser():
    return await getindivi()
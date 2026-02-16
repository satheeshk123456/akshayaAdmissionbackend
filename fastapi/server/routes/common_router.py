# routers/common_router.py
from fastapi import APIRouter, HTTPException
from ..controller.common_controller import get_user_data

router = APIRouter()

@router.get("/get-user-data/{targettable}/{userEmail}")
async def get_data(targettable: str, userEmail: str):
    data = await get_user_data(targettable, userEmail)
    
    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    return data

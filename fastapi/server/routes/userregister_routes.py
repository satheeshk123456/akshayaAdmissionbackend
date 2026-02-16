from fastapi import APIRouter
from ..model.userregister_model import User
from ..controller.userregister_controller import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def register_user(user: User):
    result = await create_user(user)
    return result

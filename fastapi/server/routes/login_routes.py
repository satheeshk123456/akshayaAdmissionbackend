from fastapi import APIRouter
from ..model.login_model import LoginModel
from ..controller.login_controller import login_user_controller

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login_user(payload: LoginModel):
    return await login_user_controller(payload)

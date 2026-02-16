from fastapi import APIRouter
from server.model.forgetpassword_model import Forgetpassmodel
from server.controller.forgetpassword_controller import forgetpasscontroller
router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/resetpassword")
async def reset_pass(userdata : Forgetpassmodel):
    return await forgetpasscontroller(userdata)
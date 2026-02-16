from fastapi import APIRouter, HTTPException
from ..model.allform_model import Allform
from ..controller.all_form_controller import save_all_form
from ..controller.all_form_controller import get_all_form_data
router=APIRouter(prefix="/allform",tags=["allform"])
@router.post("/submit")
async def submit_allform(form:Allform):
    try:
        storedformdata=await save_all_form(form)
        return{"massage":"form data submited successfully","id":storedformdata}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@router.get("/getallform")
async def get_allform(userrole_get:str,userEmail:str):
  
    data = await get_all_form_data(userrole_get,userEmail)

    if not data:
        raise HTTPException(status_code=404,details="no data found in db")
    return data    
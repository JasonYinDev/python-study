from fastapi import APIRouter,Path,HTTPException,Header,Depends,Body
from registerModels import UserSignUp

router=APIRouter(prefix="/register",tags=["注册接口"])


@router.post("",summary="注册")
def signup(form_data:UserSignUp=Body(...)):
  username=form_data.username
  password=form_data.password
  
  return {"name":username,"password":password}



from fastapi import APIRouter,Path,HTTPException,Header,Depends

router=APIRouter(prefix="/auth",tags=["权限管理"])

def auth_depend(auth:str=Header(...,description="请求头认证",alias="X-Auth")):
  if auth !="admin":
    raise HTTPException(status_code=401,detail="认证不通过")

@router.get("",summary="路径操作装饰器依赖项",dependencies=[Depends(auth_depend)])
def auth_admin():
  return {"msg":"ok"}



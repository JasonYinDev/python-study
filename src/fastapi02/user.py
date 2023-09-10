from fastapi import APIRouter,Path

router=APIRouter(prefix="/user",tags=["用户管理"])

@router.get("",summary="查看用户列表")
def get_user_list():
  return "user_list"


@router.get("/{uid}",summary="查指定用户",deprecated=True)
def get_one_user(uid:int=Path(...)):
  return f"get_one_user:{uid}"
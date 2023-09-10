from fastapi import APIRouter,Path

router=APIRouter(prefix="/profile",tags=["资料管理"])

@router.get("",summary="查看所有资料")
def get_profile_list():
  return "profile_list"


@router.get("/{uid}",summary="查指定资料")
def get_one_profile(uid:int=Path(...)):
  return f"get_one_profile:{uid}"
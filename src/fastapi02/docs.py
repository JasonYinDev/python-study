from fastapi import APIRouter,Path,Query,Depends
from typing import Dict
# from pydantic import BaseModel,Field
router=APIRouter(prefix="/page",tags=["文档查询"])


def paginator(#处理公共的页码逻辑
    page:int=Query(1,gt=0, description="当前页码"),
    page_size:int=Query(10,gt=0,lg=100,description="每页数量",alias="pageSize")         
  )-> Dict[str,int]:
  return {"page":page+1,"pageSize":page_size+1}

@router.get("",summary="查看文档列表-依赖测试")
def get_user_list(pg:Dict[str,int]=Depends(paginator)):
  return {"msg":pg}



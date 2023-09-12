from fastapi import APIRouter,Path,Query,Depends
from typing import Dict,List
# from pydantic import BaseModel,Field
router=APIRouter(prefix="/page",tags=["文档查询"])


def paginator(#处理公共的页码逻辑
    page:int=Query(1,gt=0, description="当前页码"),
    page_size:int=Query(10,gt=0,lg=100,description="每页数量",alias="pageSize")         
  )-> Dict[str,int]:
  return {"page":page+1,"pageSize":page_size+1}


def order_by_field(order_by:List[str]=Query(...,description="按给定字段排序，可以输入多个字段")):
  return {"order":order_by}

def paginator_with_order(
    pg:Dict[str,int]=Depends(paginator),
    order:List[str]=Depends(order_by_field)
  ):
  return {"pg":pg,"order":order}


@router.get("",summary="查看文档列表-依赖测试")
def get_user_list(pg:Dict[str,int]=Depends(paginator)):
  return {"msg":pg}

@router.get("/order",summary="依赖-排序功能")
def get_order(order:List[str]=Depends(order_by_field)):
  return {"msg":order}

@router.get("/pg_order",summary="依赖-分页+排序")
def get_paginator_order(pg_order:dict=Depends(paginator_with_order)):
  return {"msg":pg_order}


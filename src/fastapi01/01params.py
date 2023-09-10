import uvicorn
from fastapi import FastAPI,Path,Query,Body,Form,Header,Cookie,Request
from typing import List
from pydantic import BaseModel,Field
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

# app = FastAPI()

app = FastAPI(docs_url=None, redoc_url=None)

app.mount('/static', StaticFiles(directory='static'))

# <editor-fold desc="docs">
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger/swagger-ui.css")


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc/redoc.standalone.js")
# </editor-fold>


#添加首页
@app.get("/path/{p}",summary="path params use")
def get_path(p:str=Path(...,description="This is a required parameter")):
  return {"msg":p}

@app.get("/path/class/{cid}/student/{sid}",summary="multiple parameters")
def get_path(cid:int=Path(...,gt=0,description="class id"),sid:int=Path(...,gt=0,description="student id"),):
  return {"cid":cid,"sid":sid}

@app.get("/query",summary="query paramerter")
def get_query(q:str=Query(...,min_length=5)):
  return {"query":q}


@app.get("/query/page",summary="query paramerter - page")
def get_page(
    page:int=Query(1,description="current page"),
    page_size:int=Query(10,description="page size",alias="pageSize"),
    
  ):
  return {
    "page":page,
    "size":page_size
  }


@app.get("/query/order",summary="query paramerter - order")
def get_order(
    order:List[str]=Query(["id"],description="Sort by field (Multiple fields)"),
  ):
  return order
    



@app.post("/body/base",summary="body base use")
def post_body(p:str=Body(...)):
  return {"msg":p}


class Car(BaseModel):
  name:str=Field(...,description="name")
  brand:str=Field(...,max_length=10)
  price:float=Field(...,gt=0,example=10,description="price(10k)")

@app.post("/body/dict",summary="body - dict type")
def post_dict(p:Car=Body(...)):
  return {"dict":p}

@app.post("/body/list",summary="body - mutiple dict type")
def post_dict(p:List[Car]=Body(...)):
  return {"dict":p}

# get请求没法拿body，form等

@app.post("/form",summary="form demo")
def form_data(name:str=Form(...)):
  return name

@app.post("/header",summary="get header params")
async def get_header_params(param:str=Header(..., description="customize header",alias="Authorization")):
  """
  ## 当使用`Authorization`或者`authoriaztion`的时候docs界面不会自动发送请求头
  ## 请使用postman等测试这个接口
  """
  return {"header":param}

@app.get("/cookie",summary="get cookie params")
async def get_cookie_param(param:str=Cookie(
  None,
  alias="cookieName",
  description="customize coolie",
  example="cookie example"
)):
  return {"cookie":param}



@app.get("/req",summary="request object")
async def get_request(req:Request):
  print(req)
  return{
    "base_url":req.base_url,
    "client":req.client,
    "cookies":req.cookies,
    "headers":req.headers,
    "method":req.method,
    "path_params":req.path_params,
    "query_params":req.query_params,
    "scope":{k:str(v) for k,v in req.scope.items()},
    "url":req.url,
  }
  
  

if __name__=="__main__":
  uvicorn.run("01params:app",reload=True)
  # uvicorn.run(app) 
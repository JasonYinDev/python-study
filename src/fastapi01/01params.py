import uvicorn
from fastapi import FastAPI,Path,Query,Body
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



if __name__=="__main__":
  uvicorn.run("01params:app",reload=True)
  # uvicorn.run(app) 
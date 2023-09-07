import uvicorn
from fastapi import FastAPI
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
@app.get("/")
def index():
  return "this is home page"


@app.get("/users")
def users():
  return {
    "msg":"Get all users",
    "code":200
  }
  
@app.get("/projects")
def projects():
  return [
    "tehcui-vue2",
    "tehcui-vue3-lite",
    "tehcui-react-lite",
    "tehcui-toolkit",
  ]

if __name__=="__main__":
  uvicorn.run(app)
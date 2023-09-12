import uvicorn
from fastapi import FastAPI,Path,Query,Body,Form,Header,Cookie,Request
from typing import List
from pydantic import BaseModel,Field
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

# from .profile import router as profile_router
# from .user import router as user_router
from register import router as register_router
# from user import router as user_router
# from docs import router as docs_router
# from auth import router as auth_router
# from upload import router as upload_router


# app = FastAPI()

app = FastAPI(docs_url=None, redoc_url=None)

app.mount('/static', StaticFiles(directory='static'))

app.include_router(register_router)
# app.include_router(profile_router,deprecated=True)
# app.include_router(docs_router)
# app.include_router(auth_router)
# app.include_router(upload_router)


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



if __name__=="__main__":
  uvicorn.run("main:app",reload=True)
  # uvicorn.run(app) 
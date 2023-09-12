from fastapi import APIRouter,Query,Depends,Request
from pathlib import Path

router=APIRouter(prefix="/upload",tags=["文件上传"])


media_dir=Path(__file__).absolute().parent

# 类做依赖，可以做一些比较复杂的操作，比如在类内部定义一些关联函数被其他接口调用。
# 如果用函数定义全局变量会造成污染问题，类内部的变量则可避免污染
class FolderMaker:
  def __init__(self,upload_to:str):
    self.upload_to=upload_to
    self.dir_path=None
  def __call__(self,req:Request):
    dir_path=media_dir/self.upload_to
    # 检查目录是否存在
    self.dir_path=str(dir_path)
    return self
  
  def upload_to_disk(self):
    print("upload to cloud disk!")
  
  
@router.get("/image",summary="类做依赖，图片上传")
def upload_img(fmaker:FolderMaker=Depends(FolderMaker("image"))):
  print(fmaker.dir_path)
  fmaker.upload_to_disk()
  return {"msg":fmaker}

@router.get("/pdf",summary="类做依赖，pdf上传")
def upload_pdf(dir_name:FolderMaker=Depends(FolderMaker("pdf"))):
  return {"msg":dir_name}

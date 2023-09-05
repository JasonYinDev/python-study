import os

# os.rename("test.text","test2.text")
# os.remove("test2.text") #谨慎操作，不经过回收站

# folder
# os.mkdir("new folder")
# os.chdir("../") #改变当前代码的路径
# print(os.getcwd()) #当前路径的绝对路径
# print(os.listdir("./")) #获取当前目录的所有文件

# os.rmdir("new folder") #删除目录

# batch rename

allList=os.listdir("./test")
print(allList)
for file in allList:
  # index=file.rfind(".")
  # newName=file[:index]+"jason"+file[index:]
  newName=file.replace("jason","")
  os.rename("./test/"+file,"./test/"+newName)
  print(newName)
  print(file)
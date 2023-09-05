# file=open("./test.text","w") #创建和覆盖

# file.write("hello world")

# file.close()

# read file  如果文件不存在则报错
# file=open("test.text","r")
# content=file.read(3)
# content2=file.read(5)
# print(content)
# print(content2)

# file2=open("test.text","r")
# # line=file2.readline()
# # print(line)
# line2=file2.readlines()
# print(line2)

# backup file

file=open("./test.text","w") #创建和覆盖
file.write("hello world\n")
file.write("hello world\n")
file.close()

oldFileName=input("please input filename:")
dotIndex=oldFileName.rfind(".")
newFileName=oldFileName[0:dotIndex:]+"[bak]"+oldFileName[dotIndex:]
print(newFileName)

oldFile=open(oldFileName,"r")
newFile=open(newFileName,"w")
for line in oldFile.readlines():
  newFile.write(line)
  
oldFile.close()
newFile.close()
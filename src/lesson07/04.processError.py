# method 1
try:
  # 1/0
  print("similar js try catch")
except Exception:
  print("get error")


# method 2
try:
  # 1/0
  print("similar js try catch")
except Exception:
  print("get error")
else:
  print("if none error, run this code")
  


# method 3
finally:
  print("通常做一些收尾工作，比如文件关闭流，数据库链接关闭")
  
# advance
try:
  # 1/0
  # print("similar js try catch")
  # 手动触发上面的报错
  raise ZeroDivisionError("division by zero test")
except ZeroDivisionError as e: #捕获报错并输出
  print(e)
  
# 自定义异常类
class MyException(Exception): #自定义异常需要继承Exception这个类
  def __init__(self, min,max) -> None:
    self.min=min
    self.max=max
    
try:
  number = int(input("please input a number"))
  if not 100>=number>=10:
    raise MyException(10,100)

except ZeroDivisionError as e:
  print(e)

except MyException as e:
  print(f"Illegal number:{e}")
  
# lambda 表达式
#   参数1，参数2：代码
#   无类型，代码中不能写复杂逻辑，如return、for、if

(lambda:print("this is a lambda function"))()


a=(lambda:10+20)()
print(a)

b=(lambda num1,num2:num1*num2)(10,20)
print(b)

def login(check):
  result=check("jason","22")
  return result

result=login(lambda username,password:username+","+password)
print(result)
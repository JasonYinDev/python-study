def worker(work):
  print(work)
  
worker("test!")
worker("test!123")

def test():
  pass


def user(name,age):
  str=f"name:{name},age:{age}"
  print(str)
  return str

user("jason",18)
print(user("jason",18))


def sum(num1,num2):
  return num1+num2
def sum2(num1:int,num2:int)->int:
  return num1+num2

print(sum(100,200))
print(sum2(100,200))

def sum3(num1:int=100,num2:int=100)->int:
  return num1+num2
print(sum3())

# 多个参数，数量不确定
def test(name:str,*args):
  print(args)
  print(name)
  print(type(args))

test("aaa",1,2,3,45)

# 字典参数

def test2(**kwargs):
  print(kwargs)

test2(a=10,b=20,c=30)


def test(name:str,*args,**kwargs):
  """
  this is doc
  """
  print(f"test Start--{name}")
  print(args)
  print(type(args))
  print(kwargs)
  print(type(kwargs))

# test("aaa",1,2,3,45,a=10,b=20,c=30)


# 如果返回多个值，则会封装成tuple
def retVal(num1,num2)->tuple:
  test("aaa",1,2,3,45,a=10,b=20,c=30)
  return num1+num2,num1*num2,num1-num2

print(retVal(100,5))

print(test.__doc__)
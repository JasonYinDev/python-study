# map

newList=[]
for i in range(1,11):
  newList.append(i*i)

print(newList)

def square(x):
  return x*x
# 返回list的二次方
result=map(square,[i for i in range(1,11)])
print(list(result))


# 把字符串转为大写
names=["aaa","bbb","ccc"]
def upcase(name):
  return name.upper()
upCaseResult=map(upcase,names)
print(list(upCaseResult))



# filter
# 过滤偶数
number=[1,2,3,4,5,6,7,8]

def numFilter(x):
    return x%2==0
  
nfResult=filter(numFilter,number)
print(list(nfResult))


# reduce 

# 求出给定列表的和
from functools import reduce

def sum(num1,num2):
  return num1+num2

Rresult=reduce(sum,[i for i in range(1,11)])
print(Rresult)
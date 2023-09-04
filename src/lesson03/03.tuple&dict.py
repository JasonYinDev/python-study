# 元组的数据不能修改

name=("a","b","c")
print(name[0])
print(len(name))

#一般配合字典作为key使用



#字典 dict js object

person={
  "name":"jason",
  "age":30,
  "company":"dhc"
}

print(person)

for key in person:
  print(f"key={key}--{person[key]}")
  
#test
testArray=[1]
print(testArray*9)

array=[1,2,21,52,99,212]
print(max(array))
print(min(array))


#random String function
import string
import random
letters=string.ascii_letters
number=string.digits
print(letters)
print(number)
sum=letters+number
rdmStr="".join(random.choices(sum,k=32))
print(rdmStr)
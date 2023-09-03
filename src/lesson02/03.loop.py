# i=0
# while i<10000:
#   if i==9999:
#     print("%05d this is end"%i)
#   else: 
#     print("%05d output something"%i)
#   i+=1


# i=1
# sum=0
# while i<=10:
#   sum=sum+i
#   i+=1
  
# print("sum=%d"%sum)

# for i in range(1,11):
#   print (i)
# sum=0
# for i in range(1,11):#range 生成一个区间数组
#   sum=sum+i
  
# print (sum)

# 偶数和
# sum=0
# for i in range(1,11):#range 生成一个区间数组
#   if i%2==0:
#     sum=sum+i
#     print(f"{sum}--{i}")
    
    
# hello="hello world"
# for i in hello:
#   print(i)
  
# list=["a1","b2","c3","d4"]
# for i in list:
#   print(i)


list= range(0,11)
print(list)
print(type(list))

sum=0
for i in list:
  if i==5:
    break # 跳出循环
    # continue #继续执行，不在进行下一步else判断
  else:
    sum=sum+i
    print(sum)

# 以上代码可以精简为
# sum=0
# for i in list:
#   if i==5:
#     continue #继续执行，不在进行下一步else判断
#   sum=sum+i
#   print(sum)
# list tuple set 之间互相转换

a =[1,2,3]
aTuple=tuple(a)
aSet=set(a)
print(aTuple)
print(aSet)

b =(1,2,3)
bList=list(b)
print(bList)

# set 无默认值，需要add，无序元素

c=set()
c.add("A")
c.add("B")
c.add("B")
c.add("C")
print(c)#可以自动去重结果为{"A","B"}

cList=list(c)
print(cList)
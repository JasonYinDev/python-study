# 类型转换 int,float,str,list,tuple
# eval 和js中的eval一致 不推荐使用

a=10
a=float(a)
a=str(a)
print(type(a))

b="10.5"
b=float(b)
b=int(b)

print(type(b))
print(b)
print("="*10)

list=[1,2,3]
list = tuple(list)
print(type(list))

tuple=("a","b","c")
# tuple=list(tuple)#运行报错,因为tuple是不可变类型,反过来list是可以转为tuple的
print(type(tuple))

print(eval("3*3"))
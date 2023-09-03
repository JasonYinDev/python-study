#print("hello world!")
"""
print("hello world1!")
print("hello world2!")
多行注释
"""


typeStr="hello world"
typeList=["A","B","C"]
typeDict={"name":"a","age":16}
typeInt=100
typeFloat=100.05
# print(type(typeFloat))
# print(typeDict)

name="Jason"
age=18
weight=88.888
print("this is a %s"%name)
print("this is a %s-%d"%(name,age))
print("this is a %s-%d-%.3f"%(name,age,weight))#小数点处理%.3f 保留后三位

code=4230
print("code is %08d"%code)#在前面自动补0

# 新的一种输出方式
print(f"{name},{age},{weight}")

# %d 表示整数
# %c 字符
# %s 字符串
# %u 无符号十进制整数
# %f 浮点数
# %o 八进制整数
# %x 十六进制整数 （小写字幕0x）
# %X 十六进制整数 （大写字母0X）
# %e 科学计数法（小写e）
# %E 科学计数法（小写E）
# %g %f 和 %e 的简写
# %G %f 和 %E 的简写


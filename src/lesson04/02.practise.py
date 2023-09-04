a=10

def test():
  # global a # 提权为全局变量
  a=20
  print(a)
  
test()
print(a)

# 值引用
a=10
b=a
a=20
print(f"{a}--{b}")
print(id(a))#查看内存地址
print(id(b))

# 地址引用
a=[1,2,3,4]
b=a
a.append("test")
b.append("mark")
print(f"a{a}----b{b}")
print(id(a))
print(id(b))


# 可变和不可变

# 不可变（值传递） 数字 字符串  元组

# 可变（引用） list dict





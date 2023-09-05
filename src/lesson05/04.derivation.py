# "列表"推导式 元组 字典皆可

names1=["aaa","bbb","ccc"]
names2=("aaa","bbb","ccc")
names3={
  "A":"aaa",
  "B":"bbb",
  "C":"ccc"
}

for name in names1:
  print(name)
  
[print(names3[name]) for name in names3]
[print(f"{key}-{name}") for key,name in names3.items()]

# 以上均为列表推导式，用于快速遍历这类型容器


# 字典推导式
# 根据两个列表快速构建出一个字典
names4=["aaa","bbb","ccc","ddd"]
type1=["typeA","typeB","typeC"]

dict={key:value for key,value in zip(type1,names4)}
print(dict)
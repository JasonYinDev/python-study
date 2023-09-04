# Slice
# name="helloworld"
# print(name[0:5:])
# print(name[5:10:])
# print(name[5:10:2])

#string function

name="hello World"
print(name.capitalize())
print(name.casefold())
print(name.center(20))#左右补空格

print(name.count("l"))
print(name.count("l",0,6))#0-6限定范围

print("test.jpg".endswith("jpg"))
print("01\t01\t")
print("01\t01\t".expandtabs())


print("hello {0}".format("world"))

class Default(dict):
  def __missing__(self,key):
    return "China"
print('{name} was born in {country}'.format_map(Default(name="Jason")))

print(name.find("llo1")) #查找位置相当于indexOf，不存在的话返回-1
print(name.index("llo")) # 不存在的话报错
print("a,b,c,d".partition(","))
print("a,b,c,d".split(","))

# str.upper(): 返回字符串的大写版本。
# str.lower(): 返回字符串的小写版本。
# str.capitalize(): 返回字符串的首字母大写版本。
# str.title(): 返回字符串中每个单词的首字母大写版本。
# str.swapcase(): 返回字符串中大小写互换的版本。
# str.strip(): 移除字符串两端的空白字符。
# str.lstrip(): 移除字符串左侧的空白字符。
# str.rstrip(): 移除字符串右侧的空白字符。
# str.startswith(prefix): 检查字符串是否以指定前缀开头。
# str.endswith(suffix): 检查字符串是否以指定后缀结尾。
# str.replace(old, new): 将字符串中的旧子串替换为新子串。
# str.split(separator): 将字符串分割成子字符串的列表，使用分隔符进行分割。
# str.join(iterable): 使用字符串作为连接符，将可迭代对象中的元素连接成一个字符串。
# str.find(substring): 查找子字符串在字符串中的第一个位置。
# str.rfind(substring): 查找子字符串在字符串中的最后一个位置。
# str.index(substring): 查找子字符串在字符串中的第一个位置，如果未找到则引发异常。
# str.count(substring): 统计子字符串在字符串中出现的次数。
# str.isalpha(): 检查字符串是否只包含字母字符。
# str.isdigit(): 检查字符串是否只包含数字字符。
# str.isalnum(): 检查字符串是否只包含字母和数字字符。
# str.islower(): 检查字符串是否全部为小写字母。
# str.isupper(): 检查字符串是否全部为大写字母。
# str.isnumeric(): 检查字符串是否只包含数字字符（包括Unicode数字字符）。
# str.isdecimal(): 检查字符串是否只包含十进制数字字符。
# str.startswith(tuple): 检查字符串是否以元组中任何一个元素作为前缀。

print(name[::-1]) #字符串反转
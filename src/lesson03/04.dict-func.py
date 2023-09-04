person={
  "name":"jason",
  "age":30,
  "company":"dhc"
}

person["sex"]="male"
print(person)
print("sex" in person)

del person["sex"]
print(person)
print("sex" in person)

#get all keys
print(person.keys())
print(person.values())
print(person.items()) #转换为元组

for key,value in person.items():
  print(f"key:{key}-value:{value}")
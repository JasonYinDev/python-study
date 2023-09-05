

def showMenu():
  print("-----------------User Managerment-----------------")
  print("1-Add User")
  print("2-Delete User")
  print("3-Edit User")
  print("4-Inquire User")
  print("5-List All User")
  print("6-Exit")
  
userList=[
  {"name":"jason","age":18,"phone":"188322123"}
]
def addUser():
  name=input("input name:")
  age=input("input age:")
  phone=input("input phone:")
  userDict={
    "name":name,
    "age":age,
    "phone":phone,
  }
  userList.append(userDict)

def editUser(index):
  name=input("input name:")
  age=input("input age:")
  phone=input("input phone:")
  userDict={
    "name":name,
    "age":age,
    "phone":phone,
  }
  userList[index]=userDict

def deleteUser(index):
  if index>-1 and index<=len(userList)-1:
    # del userList[index]
    userList.pop(index)
    print("del success")
  else:
    print("can't find user index")
  
def showAllUser():
  # for index,user in enumerate(userList):
  #   print(f"index:{index}----name:{user['name']},age:{user['age']},phone:{user['phone']}")
  for user in userList:
    print(f"index:{userList.index(user)}----name:{user['name']},age:{user['age']},phone:{user['phone']}")

def inquire(index):
  print(f"index:{index}----name:{userList[index]['name']},age:{userList[index]['age']},phone:{userList[index]['phone']}")
  # print(userList[index])


def main():
  while True:
    showMenu()
    choice=input("please the action")
    if choice=="1":
      addUser()
      print("add")
    elif choice=="2":
      showAllUser()
      index=int(input("input index:"))
      deleteUser(index)
    elif choice=="3":
      showAllUser()
      index=int(input("input index:"))
      editUser(index)
      print("edit")
    elif choice=="4":
      showAllUser()
      index=int(input("input index:"))
      inquire(index)
      # print("inquire")
    elif choice=="5":
      showAllUser()
      print("list")
    elif choice=="6":
      print("exit")
      break
      # exit(0)
    else:
      print("error")
    
    
main()
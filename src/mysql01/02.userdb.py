import pymysql


def register():
  print("用户注册")
  user=input("请输入用户名: ")
  password=input("请输入密码: ")

  conn =pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="passw0rd",charset="utf8", db="userdb")
  cursor=conn.cursor()

  sql= f"insert into users (name,password) values('{user}','{password}')"
  cursor.execute(sql)
  conn.commit()
  
  cursor.close()
  conn.close()
  
  print(f"注册成功,用户名:{user},密码:{password}")


def login():
  print("用户登录")
  user=input("请输入用户名: ")
  password=input("请输入密码: ")

  conn =pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="passw0rd",charset="utf8", db="userdb")
  cursor=conn.cursor()
  
  # 以下这种写法会造成sql注入漏洞，比如 user的位置输入 ' or 1=1 --
  # sql= f"select * from users where name='{user}' and password='{password}'"
  # sql 注入攻击后，显示为如下条件
  # sql= f"select * from users where name='' or 1=1 --' and password='123'"
  # cursor.execute(sql)
  
  # 避免sql注入攻击，应该使用下面的方法
  # cursor.execute("select * from users where name=%s and password=%s",[user,password])
  # 另外一种写法
  cursor.execute("select * from users where name=%(user)s and password=%(password)s",{"user":user,"password":password})
  
  
  result=cursor.fetchone()
  cursor.close()
  conn.close()

  if result:
    print("登录成功",result)
  else:
    print("登录失败")
    
    
def run():
  choice=input("1.注册；2.登录; 请输入：")
  if choice =="1":
    register()
  elif choice =="2":
    login()
  else:
    print("输入错误")
    
if __name__=="__main__":
  run()
import pymysql

# 链接数据库
conn =pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="passw0rd",charset="utf8")
cursor=conn.cursor()

# 创建数据库
# cursor.execute("create database db4 default charset utf8 collate utf8_general_ci")
# conn.commit()

# 进入数据库
cursor.execute("use mysqlstudy")
cursor.execute("show tables")
result=cursor.fetchall()
print(result)

# 进入数据库创建表
sql="""
create table L3(
  id int not null primary key auto_increment,
  title varchar(123),
  content text,
  ctime datetime
)default charset=utf8;
"""
# cursor.execute(sql)
# conn.commit()

cursor.execute("show tables")
result=cursor.fetchall()
print(result)

# 关闭链接
cursor.close()
conn.close()

class Employee(object):
  adress="shanxi"
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def __str__(self) -> str:
    return f"name:{self.name},id:{self.id}"
  def work(self):
    print(f"name:{self.name},id:{self.id} employee is working")
    
class Teacher(Employee):
  def __init__(self,name, id, course):
    # super().__init__(name, id) 
    super(Teacher,self).__init__(name, id)  # 调用父类的构造函数初始化name和id
    self.course=course
  def lecture(self):
    super().work()
    print(f"name:{self.name},id:{self.id} lecture:{self.course}")
  
class HeadTeacher(Employee):
  def __init__(self,name, id, management ):
    super(HeadTeacher,self).__init__(name,id)
    self.management=management
  def manage(self):
    print(f"name:{self.name},id:{self.id} manage:{self.management}")
    

  

tc01=Teacher("jason",33,"math")
print(tc01)
tc01.lecture()

# tc02=HeadTeacher("aYin",88,"classroom order")
# tc02.manage()


# not working
# class SubstituteTeacher(Teacher, HeadTeacher):
#     def __init__(self, name, id, course, management):
#       # 调用Teacher和HeadTeacher的构造函数来初始化相应属性
#       Teacher.__init__(self, name, id, course)
#       HeadTeacher.__init__(self, name, id, management)
#     def __str__(self):
#       return f"name:{self.name}, id:{self.id}, course:{self.course}, manage:{self.management}"
#     # 如果需要在代课老师类中添加额外的方法，可以在这里定义
#     def substitute(self):
#       print(f"name:{self.name}, id:{self.id}, course:{self.course}, manage:{self.management}")

# st01=SubstituteTeacher("emils",99,"CS","home work")
# print(st01)
# st01.substitute()
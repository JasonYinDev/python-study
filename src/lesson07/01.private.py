class Employee(object):
  def __init__(self,name,id,pirv):
    self.name=name
    self.id=id
    self.__pirv=pirv
  def __str__(self) -> str:
    self.__privFunc()
    return f"name:{self.name},id:{self.id}"
  def work(self):
    print(f"name:{self.name},id:{self.id}  employee is working pirv:{self.__pirv}")
  def __privFunc(self):#私有方法仅仅内在类的内部调用
    print(f"privfunction:{self.__pirv}")
class Teacher(Employee):
  def __init__(self,name, id,pirv, course):
    # super().__init__(name, id) 
    super(Teacher,self).__init__(name, id,pirv)  # 调用父类的构造函数初始化name和id
    self.course=course
  def lecture(self):
    super().work()
    print(f"name:{self.name},id:{self.id} lecture:{self.course}")
  
  
tc01=Teacher("jason",33,"private","math")
print(tc01)
# print(tc01.__pirv)#私有属性无法访问
tc01.lecture()

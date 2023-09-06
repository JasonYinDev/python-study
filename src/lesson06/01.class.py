# 和js中的class没有区别
class Person(object):
  # 属性 行为  类似js中的类
  def __init__(self):
    self.location="China"
    print("creat person")
  def playGame(self,game):
    self.game=game
    print(f"{self.name} play-{game} location-{self.location}")
  def __str__(self):
    return self.name 
    
  #当程序运行结束后会调用的方法
  def __del__(self):#所有的对象删除后才执行此方法
    print("del")
newPerson=Person()
newPerson.name="jason"
newPerson.sex="male"
newPerson.age=18

newPerson.playGame("lol")
# del newPerson #这里直接销毁，后面代码无法执行
print(f"{newPerson.name}--{newPerson.game}")
print(f"str return--{newPerson}")



class Computer(object):
    def __init__(self,cpu,graCard,memory):
      self.cpu=cpu
      self.graCard=graCard
      self.memory=memory
    
    def useComputer(self,operate):
      if operate=="play":
        if self.graCard=="3070":
          self.performance="high"
          print("can play game")
        elif self.graCard=="1060":
          self.performance="low"
          print("bad experience")
        else:
          self.performance="unknow"
          print("unknow")
      elif operate=="work":
        if self.cpu=="i9":
          self.performance="high"
        if self.cpu=="i7":
          self.performance="good"
        if self.cpu=="i5":
          self.performance="normal"
        if self.cpu=="i3":
          self.performance="low"
          
    def __str__(self):
      return self.performance
      
comp01=Computer("i9","3070",16)
comp01.useComputer("play")
print(f"game performance {comp01.performance}")

comp02=Computer("i3","1060",16)
comp02.useComputer("work")
print(f"work performance {comp02.performance}")



print("--------------------")

class User(object):
  def __init__(self,name,phone):
    self.name=name
    self.phone=phone
  
  def usePhone(self):
    self.phone.zhihu(self.name)

class Phone(object):
  def __init__(self,phoneType):
    self.type=phoneType
  def zhihu(self,user):
    print(f"user:{user} use mobile:{self.type} open zhihu")
    
phone=Phone("iphone")
user=User("jason",phone)
user.usePhone()

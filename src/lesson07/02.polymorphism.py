# 多态特点
  # 1.必须有继承关系
  # 2.子类必须重写父类的方法

class Fater (object):
  def spand(self):
    print("father spand money")
    
class Son(Fater):
  def spand(self):
    print("Son spand money")
    
def buyTV(who):
  who.spand()
  
# buyTV(Fater())
buyTV(Son())
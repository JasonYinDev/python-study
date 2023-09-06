class Person(object):
  # object function #创建对象的时候才生效
  def eat(self):
    print("must eat")
  # object private function
  def __study(self):
    print("should study")
    
  # class function #创建类的时候就生效
  @classmethod
  def fly(self):
    print("can't fly")
    
  @classmethod #
  def run(self):
    print("can run")
    
  @staticmethod #独立于类的一个方法，仅仅被这个类限定了作用域 可被外部访问，但内部无法访问self
  def sleep():
    print("can sleep")
user=Person()
user.eat()
# user.__study()#can not call
user.fly()
Person.fly()
# Person.eat()#can not call


# 生命周期 ：  静态方法 > 类方法 > 对象方法
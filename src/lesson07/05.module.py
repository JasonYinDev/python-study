
# from test import Person,Animal,test1,test2
from test import *  #告警但是能正常运行

newPerson=Person()
newPerson.name="jason"
newPerson.sex="male"
newPerson.age=18

newPerson.playGame("lol")
print(newPerson)

print("-----------------------------")

import test

newPerson2=test.Person()
newPerson2.name="jason"
newPerson2.sex="male"
newPerson2.age=18

newPerson2.playGame("lol")
print(newPerson2)


from os import getcwd
print(getcwd())

import os
print(os.getcwd())

import os as myos
print(myos.getcwd())


Animal().eat()
test1()
# test2()
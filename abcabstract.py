#activity1
from abc import ABC,abstractmethod

class absclass(ABC):
    def print(self,x):
        print("passed var:",x)
    @abstractmethod
    def task(self):
        print("we are in abclass task")
class test(absclass):
    def task(self):
        print("we are in test task")
test_obj=test()
test_obj.task
test_obj.print(100)
#activity2
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk around")
class snake(animal):
    def move(self):
        print("I can slither around")
class monkey(animal):
    def move(self):
        print("I can swing around")

Q=human()
Q.move()
W=snake()
W.move()
E=monkey()
E.move()
#activity3
class UAE():
    def cap(self):
        print("Dubai")
    def lan(self):
        print("Arabic and English")
    def type(self):
        print("UAE is a developed contury")
class Pakistan():
    def cap(self):
        print("Lahore")
    def lan(self):
        print("Arabic and Urdu")
    def type(self):
        print("Pakistan is a developing contury")

obj_UA=UAE()
obj_Pak=Pakistan()
for contury in (obj_UA,obj_Pak):
    contury.cap()
    contury.lan()
    contury.type()
#activity1
class veicle:
    def __init__(self,name,speed,milage):
        self.name=name
        self.speed=speed
        self.milage=milage
class bus(veicle):
    pass
bus1=bus("Volvo",120,10)
print("Name of the bus is: ",bus1.name)
print("Speed of the bus is: ",bus1.speed)
print("Milage of the bus is: ",bus1.milage)
#activity2
class person:
    def __init__ (self,name,idnum):
        self.name=name
        self.idnum=idnum
    def display(self):
        print(self.name)
        print(self.idnum)
class employe(person):
    def __init__(self,name,idnum,salery,post):
        self.salery=salery
        self.post=post
        person.__init__(self,name,idnum)

obj=employe("postman",50,8900,"intern")
print(obj.name)
print(obj.idnum)
print(obj.salery)
print(obj.post)
#activity3
class bird:
    def __init__(self):
        print("bird is ready")
    def sqwack(self):
        print("sqwack sqwak")
    def swim(self):
        print("swim faster")

class penguin(bird):
    
#activity1
class myclass():
    __privar=27

    def __primeth(self):
        print("im in class myclass")

    def hello(self):
        print(myclass.__privar)

foo=myclass()
foo.hello()
#foo.__primeth()
#activity2
class computer():
    def __init__(self,maxprice=900):
        self.__maxprice=maxprice

    def changeprice(self,new):
        self.__maxprice = new
        print(self.__maxprice)

    def price(self):
        print(self.__maxprice)

c=computer(900)
print(c.price())
print(c.price())
c.changeprice(1000)
print(c.price())
#activity3
class points():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def retur(self):
        return "{1},{2}".format(self.x,self.y)

p1=points(2,3)
print(p1)
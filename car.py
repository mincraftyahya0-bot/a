class BMW():
    def mil(self):
        print(35)
    def speed(self):
        print("155 mph")
    def size(self):
        print("4,500 mm")
class Ferari():
    def mil(self):
        print(27)
    def speed(self):
        print("359 kmph")
    def size(self):
        print("4,565 x 1,958 x 1,187 mm")

obj_BM=BMW()
obj_fer=Ferari()
for contury in (obj_BM,obj_fer):
    contury.mil()
    contury.speed()
    contury.size()
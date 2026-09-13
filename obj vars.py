#activity1
class grade4:
    grade = 4
    print("This is class", grade)
obj = grade4()
print(obj.grade)
#activity2
class car:
    def __init__(self,maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

obj = car(200, 15)
print("Max Speed:", obj.maxspeed)
print("Mileage:", obj.mileage)
#activity3
class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
woo=parrot("Woo", 10)
bob=parrot("Bob", 15)
print("species:", woo.species,bob.species)
print("name:", woo.name,bob.name)
print("age:", woo.age,bob.age)

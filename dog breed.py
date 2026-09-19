class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Brown")

print("Dog 1:")
print("Animal:", dog1.animal)
print("Breed:", dog1.breed)
print("Colour:", dog1.colour)

print()

print("Dog 2:")
print("Animal:", dog2.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)
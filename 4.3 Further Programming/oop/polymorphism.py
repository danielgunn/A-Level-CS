class Pet:
    def petIt(self):
        print(" ❤ ")

class Dog(Pet):
    def petIt(self):
        print("wags tail")
        Pet.petIt(self)

class Cat(Pet):
    def petIt(self):
        print("Scratch!!")

pets = [Dog(), Cat()]

for p in pets:
    p.petIt()
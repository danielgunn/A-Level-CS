from random import randint
class Cat:
    __mood = "hungry"

    def timePasses(self):
        moods = ["a little angry", "angry", "hungry", "very angry"]
        self.__mood = moods[randint(0, 4)]

    def petIt(self):
        if self.__mood == "hungry":
            print("purr...")
        else:
            print("Scratch!!")

c = Cat()
c.timePasses()
if c.__mood == "hungry":
    c.petIt()
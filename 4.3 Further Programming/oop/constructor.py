class Animal():
    def __init__(self, name):
        self.__name = name
        self.__heartbeats = 0
        self.__alive = True

    def getName(self):
        return self.__name

    def move(self):
        if self.__alive:
            self.__heartbeats += 1

a = Animal("Lucky")
a.move()
print(a.getName())
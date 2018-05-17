class Toy:
    def __init__(self,name,id,price,minAge):
        Toy.setName(self,name)
        Toy.setID(self,id)
        Toy.setPrice(self,price)
        Toy.setMinAge(self,minAge)
    
    def getID(self):
        return self._id

    def setID(self, id):
        if not isinstance(id, str):
            raise ValueError("id must be string")
        if len(id) < 1:
            raise ValueError("id must be 8 characters", id)
        self._id = id


    def getName(self):
        return self._name
    
    def setName(self, name):
        if not isinstance(name, str):
            raise ValueError("name must be string")
        if len(name) < 1:
            raise ValueError("invalid name", name)
        self._name = name
    
    def getPrice(self):
        return self._price
    
    def setPrice(self,price):
        if price < 0:
            raise ValueError("price must be positive")
        self._price = price
    
    def getMinAge(self):
        return self._minAge
    
    def setMinAge(self, minAge):
        if minAge < 0:
            raise ValueError("minAge must be positive")
        if minAge > 18:
            raise ValueError("minAge too old")
        self._minAge = minAge

class ComputerGame(Toy):
    def __init__(self, name, id, price, minAge, category, console):
        Toy.__init__(self, name, id, price, minAge)
        self._category = category
        self._console = console
    
    def getCategory(self):
        return self._category
    
    def setCategory(self, category):
        self._category = category
    
    def getConsole(self):
        return self._console
    
    def setConsole(self, console):
        self._console = console

class Vehicle(Toy):
    def __init__(self, name, id, price, minAge, type, height, length, weight):
        Toy.__init__(self, name, id, price, minAge)
        self._type = type
        self._height = height
        self._length = length
        self._weight = __weight
    
    def getType(self):
        return self._type
    
    def getHeight(self):
        return self._height

    def getLength(self):
        return self._length
    
    def getWeight(self):
        return self._weight
    
    def setHeight(self, height):
        self._height = height
    
    def setLength(self, length):
        self._length = length
    
    def setWeight(self, weight):
        self._weight = weight

    def setHeight(self, height):
        self._height = height

ball = Toy("ball","b1",20, 1)
frisbee = Toy("frisbee", "f1", 10, 3)
l4d = ComputerGame("l4d", "l4d", 10, 15, "FPS", "PC")


assert(ball.getName() == "ball")
ball.setName("Ball")
assert(ball.getName() == "Ball")

assert(frisbee.getPrice() == 10)
frisbee.setPrice(11)
assert(frisbee.getPrice() == 11)

assert(ball.getMinAge() == 1)
ball.setMinAge(2)
assert(ball.getMinAge() == 2)

print("All tests passed")
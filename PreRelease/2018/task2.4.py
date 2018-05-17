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

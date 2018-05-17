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
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} [{}] \n Price: ${:.2f} \n MinAge: {}".format(
            self._name, 
            self._id, 
            self._price, 
            self._minAge)
        
    def discount(self, amount):
        d = (100-amount)/ 100
        self.setPrice(self._price * d)

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

    """def __str__(self):
        return "{}\n {} \n {} game".format(
            Toy.__str__(self),
            self._category, 
            self._console)"""
    
    def __str__(self):
        return str(Toy.getPrice(self))
        
    

class Vehicle(Toy):
    def __init__(self, name, id, price, minAge, type, height, length, weight):
        Toy.__init__(self, name, id, price, minAge)
        Vehicle.setWeight(self, weight)
        Vehicle.setType(self, type)
        Vehicle.setLength(self, length)
        Vehicle.setHeight(self, height)
    
    def getType(self):
        return self._type
    
    def getHeight(self):
        return self._height

    def getLength(self):
        return self._length
    
    def getWeight(self):
        return self._weight
    
    def setType(self, type):
        self._type = type

    def setHeight(self, height):
        self._height = height
    
    def setLength(self, length):
        self._length = length
    
    def setWeight(self, weight):
        self._weight = weight

    def setHeight(self, height):
        self._height = height
    
    """def __str__(self):
        return "{}\n {} [{} x {} x {}]".format(
            Toy.__str__(self), 
            self._type, 
            self._height, 
            self._length, 
            self._weight)"""

    def __str__(self):
        return str(Toy.getPrice(self))

def findToy():
    id = input("Enter the toy ID:")
    for t in toys:
        if (t.getID() == id):
            print(t)
            exit()
    print("Toy with id `" + id + "` not found")

def bubbleSortToys(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j].getPrice() > arr[j + 1].getPrice():
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def insertionSortToys(arr):
    N = len(arr)
    for i in range(1, N):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp.getPrice() < arr[j].getPrice():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


rsc = Vehicle("Red Sports Car", "RSC13", 15.0, 6, "Car", 3.3, 12.1, 0.08)
l4d = ComputerGame("l4d", "L4D01", 10, 15, "FPS", "PC")
l4d.discount(20)

toys = []
toys.append(rsc)
toys.append(l4d)

toys.append(Vehicle("ABC", "ABC", 5, 1, "ABC", 1, 1, 1))
toys.append(ComputerGame("CDE","CDE",2,2,"CDE", "CDE"))
toys.append(Vehicle("DEF", "DEF", 1, 3, "DEF", 3,3,3))

print("before sort")
print(toys)
print()

print("after sort")
insertionSortToys(toys)
print(toys)

#findToy()


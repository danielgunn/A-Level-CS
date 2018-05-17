class Toy:
    def __init__(self,name,price,minAge):
        Toy.setName(self,name)
        Toy.setPrice(self,price)
        Toy.setMinAge(self,minAge)
    
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

ball = Toy("ball",20, 0)
frisbee = Toy("frisbee", 10, 3)


assert(ball.getName() == "ball")
ball.setName("Ball")
assert(ball.getName() == "Ball")

assert(frisbee.getPrice() == 10)
frisbee.setPrice(11)
assert(frisbee.getPrice() == 11)

assert(ball.getMinAge() == 0)
ball.setMinAge(-1)
assert(ball.getMinAge() == 2)

print("All tests passed")
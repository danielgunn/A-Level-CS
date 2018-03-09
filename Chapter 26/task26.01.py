import pickle
from datetime import date

# My solution for task 26.01
# @author Daniel Gunn

class Car:
    def __init__(self, vid, reg, dor, es, pp):
        self.__vehicleID = vid
        self.__registration = reg
        self.__dor = dor
        self.__engineSize = es
        self.__purchasePrice = pp

    def __str__(self):
        return "** Vehicle {} **\n{}\n{}\n{}\n{}\n*********".format(
            self.__vehicleID,self.__registration,self.__dor,self.__engineSize,self.__purchasePrice)

cars = [
    Car("V01", "R01", date(2011,1,11), 1600, 10000),
    Car("V02", "R02", date(2012,2,12), 1700, 11000),
    Car("V03", "R03", date(2013,3,13), 1800, 12000),
    Car("V04", "R04", date(2014,4,14), 1900, 13000),
    Car("V05", "R05", date(2015,5,15), 2000, 14000)]


f = open("cars.dat", "wb")
for c in cars:
    pickle.dump(c, f)
f.close()

f = open("cars.dat", "rb")
while (True):
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()
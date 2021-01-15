import pickle
from datetime import date

# My solution for task 26.02
# @author Daniel Gunn

NUM_RECORDS = 10
RECORDS_FILE = "cars.dat"

def hash(vid):
    t = 0
    for c in vid:
        t += ord(c)
    t %= NUM_RECORDS
    return t

class Car:
    def __init__(self, vid, reg, dor, es, pp):
        self.__vehicleID = vid
        self.__registration = reg
        self.__dor = dor
        self.__engineSize = es
        self.__purchasePrice = pp

    def getVID(self):
        return self.__vehicleID

    def __str__(self):
        return "** Vehicle {} **\n{}\n{}\n{}\n{}\n*********".format(
            self.__vehicleID,self.__registration,self.__dor,self.__engineSize,self.__purchasePrice)

cars = [
    Car("V01", "R01", date(2011,1,11), 1600, 10000),
    Car("V02", "R02", date(2012,2,12), 1700, 11000),
    Car("V10", "R03", date(2013,3,13), 1800, 12000),
    Car("V04", "R04", date(2014,4,14), 1900, 13000),
    Car("V05", "R05", date(2015,5,15), 2000, 14000)]

# Note Car V01 and V10 will collide!

# Determine how large (in bytes) each car record in
# NOTE: here we assume all records are the same size!
CAR_SIZE = len(pickle.dumps(cars[0]))

# initialize the random access file containing records
f = open(RECORDS_FILE, "wb")
for i in range(0, NUM_RECORDS):
    f.seek(CAR_SIZE * i)
    pickle.dump(None,f)
f.close()

# Input the car records into the file
f = open(RECORDS_FILE, "rb+")
for c in cars:
    addr = hash(c.getVID())
    c2 = 0
    while (c2 != None):
        f.seek(CAR_SIZE * addr)
        c2 = pickle.load(f)
        if (c2 != None):
            print(c.getVID(), "collided with", c2.getVID())
            addr += 1
            addr %= NUM_RECORDS
    print(c.getVID(), "placed at address", addr)
    f.seek(CAR_SIZE * addr)
    pickle.dump(c,f)
f.close()

# Search for user given vehicle id
f = open(RECORDS_FILE, "rb+")
vid = None
while (True):
    vid = input("Enter Vehicle ID (Q for Quit):")
    if (vid == "Q"):
        break
    addr = hash(vid)
    while(True):
        f.seek(addr * CAR_SIZE)
        c = pickle.load(f)
        if (c == None):
            print("not found at ", addr)
            break
        if (c.getVID() == vid):
            print(c)
            break
        else:
            addr += 1
            addr %= NUM_RECORDS
f.close()
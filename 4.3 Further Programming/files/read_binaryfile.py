import pickle
from record_student import Student

f = open("myrecords.dat","rb")
b = pickle.load(f)
print(b.getName(), "read from file")
f.close()
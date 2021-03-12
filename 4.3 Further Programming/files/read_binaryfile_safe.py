import pickle
from record_student import Student

try:
    f = open("myrecords.dat","rb")
    b = pickle.load(f)
    print(b.getName(), "read from file")
    f.close()
except FileNotFoundError:
    print("File doesnt exist")
except:
    print("Something unknown happened")
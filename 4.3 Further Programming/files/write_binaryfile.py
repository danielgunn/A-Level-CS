import pickle
from record_student import Student

a = Student("James")

f = open("myrecords.dat","wb")
pickle.dump(a,f)
f.close()

print("student saved")
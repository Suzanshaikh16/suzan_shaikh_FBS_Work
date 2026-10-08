import pickle
class Student:
    def __init__(self, rollno, name, batch):
        self.rollNo = rollno
        self.name = name
        self.batch = batch
    def getRollNo(self):
        return self.rollNo
    def setRollNo(self, nrollno):
        self.rollNo = nrollno
    def __str__(self):
        return f"{self.rollNo} {self.name} {self.batch}"
# Normal text file
s1 = Student(12, "Swarup", 55)
f = open("xyz.txt", "w")
f.write(str(s1))
f.close()
fr = open("xyz.txt", "r")
data = fr.read()
fr.close()
print(data)
print(type(data))
# Pickle file
s1 = Student(1, "Rahul", 45)
s2 = Student(2, "Swarup", 55)
s3 = Student(3, "Amit", 65)
f = open("xyz.dat", "wb")
pickle.dump(s1, f)
pickle.dump(s2, f)
pickle.dump(s3, f)
f.close()
# Reading objects
fr = open("xyz.dat", "rb")
d1 = pickle.load(fr)
d2 = pickle.load(fr)
d3 = pickle.load(fr)
print(d1)
print(d2)
print(d3)
print(type(d1))
fr.close()
# Append another object
f = open("xyz.dat", "ab")
pickle.dump(Student(4, "Rahul", 45), f)
print(f.tell())
f.close()
# Read the newly added object
fr = open("xyz.dat", "rb")
d1 = pickle.load(fr)
d2 = pickle.load(fr)
d3 = pickle.load(fr)
d4 = pickle.load(fr)
print(d4)
fr.close()
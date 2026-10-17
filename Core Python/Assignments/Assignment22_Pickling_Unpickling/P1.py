import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.ename)
        print("Basic Salary:", self.basic)


e1 = Emp(101, "Suzan", 25000)

# Pickling
f = open("emp.dat", "wb")
pickle.dump(e1, f)
f.close()

# Unpickling
f = open("emp.dat", "rb")
e2 = pickle.load(f)
f.close()

e2.display()
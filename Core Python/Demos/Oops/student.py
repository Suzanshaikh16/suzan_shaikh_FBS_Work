class Student:
    inName = "FBS"
    stdCount = 0

    def __init__(self, rollno, name, batch):
        self.rollNo = rollno
        self.name = name
        self.batch = batch
        Student.stdCount += 1

    def setRollno(self, nron):
        self.rollNo = nron

    def display(self):
        print(f"RollNo={self.rollNo}\t Name={self.name}\t Batch={self.batch}\t Institute Name={Student.inName}")


class PlaceedStudent(Student):
    def __init__(self, rollno, name, batch, cName):
        super().__init__(rollno, name, batch)
        self.cName = cName

    def display(self):
        print(f"CName={self.cName}")
        return super().display()


s1 = Student(12, "Suraj", 1234)
s2 = PlaceedStudent(1, "Shankar", 1232, "GlobalPyment")

print(Student.stdCount)
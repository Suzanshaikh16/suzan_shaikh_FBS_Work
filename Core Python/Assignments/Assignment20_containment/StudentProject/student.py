from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks


class Student:
    def __init__(self, rollno, name, sy, ty):
        self.rollno = rollno
        self.name = name
        self.sy = sy
        self.ty = ty

    def CalculateGrade(self):
        total = self.sy.ComputerTotal + self.ty.Theory + self.ty.Practical
        percentage = total / 3

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\n----- Student Result -----")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("SY Computer Marks:", self.sy.ComputerTotal)
        print("TY Theory Marks:", self.ty.Theory)
        print("TY Practical Marks:", self.ty.Practical)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


sy = SYMARKS(75, 80, 70)
ty = TYMarks(65, 70)

s1 = Student(101, "Rahul", sy, ty)
s1.CalculateGrade()
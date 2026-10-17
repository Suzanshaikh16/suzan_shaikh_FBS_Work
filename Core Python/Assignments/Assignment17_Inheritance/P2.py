class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    def CalculateRank(self):
        if self.Percentage >= 75:
            print("Rank: Distinction")
        elif self.Percentage >= 60:
            print("Rank: First Class")
        elif self.Percentage >= 50:
            print("Rank: Second Class")
        elif self.Percentage >= 35:
            print("Rank: Pass Class")
        else:
            print("Rank: Fail")

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"


class EnggStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def CalculateRank(self):
        if self.Percentage >= 75 and self.InternalMarks >= 40:
            print("Rank: Distinction")
        elif self.Percentage >= 60:
            print("Rank: First Class")
        elif self.Percentage >= 50:
            print("Rank: Second Class")
        elif self.Percentage >= 35:
            print("Rank: Pass Class")
        else:
            print("Rank: Fail")

    def __str__(self):
        return super().__str__() + f", {self.Branch}, {self.InternalMarks}"


e1 = EnggStudent(101, "Smita", 21, 85.5, "Computer", 45)

e1.Display()
e1.CalculateRank()
print(e1)
class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId=StudentId
        self.Name=Name
        self.Age=Age
        self.Percentage=Percentage

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
        return f"Student ID:{self.StudentId},Name:{self.Name},Age:{self.Age},Percentage:{self.Percentage}"


s1 = Student(101,"Alice",21,85.5)

s1.Display()
s1.CalculateRank()

print(s1)
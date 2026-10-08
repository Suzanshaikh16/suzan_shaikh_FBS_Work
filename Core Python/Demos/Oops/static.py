class Student:
    inNames='FBS'
    @staticmethod
    def Greet():
        print('Welcome...........')
        
    def __init__(self,rollno,name,batch):
        self.rollno=rollno
        self.name=name
        self.batch=batch
    def display(self):
        print(f"RollNo={self.rollno}\tName={self.name}\tBatch={self.batch}\tInstitute Name={self.inNames}\t")
s1=Student(12,'Suraj','Julypython')
s2=Student(13,'Smita','Junepython')
s3=Student(14,'Sofi','Java')
s1.display()
s2.display()
s3.display()
s1.inNames='FirstbitSolutions'
Student.inNames='FirstbitSolutions'
print('***********************************')
s1.display()
s2.display()
s3.display()
Student.Greet()
s1.Greet()
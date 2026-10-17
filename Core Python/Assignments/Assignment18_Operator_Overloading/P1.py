class ComplexNumber:

    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag

    def __del__(self):
        print("Object destroyed")

    def __add__(self, other):
        r=self.real + other.real
        i=self.imag + other.imag
        return ComplexNumber(r,i)

    def __sub__(self, other):
        r=self.real-other.real
        i=self.imag-other.imag
        return ComplexNumber(r,i)

    def display(self):
        print(self.real,"+",self.imag,"i")


c1=ComplexNumber(10,5)
c2=ComplexNumber(4,2)

c3=c1+c2
c4=c1-c2

print("Addition:")
c3.display()

print("Subtraction:")
c4.display()
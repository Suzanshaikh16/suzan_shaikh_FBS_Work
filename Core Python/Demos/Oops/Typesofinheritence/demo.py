class Emp:
    def __init__(self, nm):
        self.name = nm

    def display(self):
        print("Display")
# Emp ends here....
class Devloper(Emp):

    def display(self):
        print("Display of Dev")
# Dev ends here....
class HR(Emp):
    def display(self):
        print("Display of HR")
# HR ends here....
class JrHR(HR):
    def display(self):
        print("I am from display of Jr HR")
# Jr HR ends here....
class SrHR(HR):
    def display(self):
        print("I am from display of Sr HR")
# Sr HR ends here....
class JrDev(Devloper):
    def display(self):
        print("I am from display of Jr Developer")
# Jr Dev ends here....
# Creating objects
jhr = JrHR("Smriti")
jhr.display()
jrd = JrDev("Sachin")
jrd.display()

class Mec:
    def display(self):
        print("Mec")
class Electric:
    def display(self):
        print("I am from Electrical")
class Mecatronix(Electric, Mec):
    def abc(self):
        print("I am in mechatronix")
m = Mecatronix()
m.display()

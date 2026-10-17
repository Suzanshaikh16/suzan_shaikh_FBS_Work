
class Shirt:
    price_change=10 

    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

        if size.lower()=="medium":
            self.price=price+(price*Shirt.price_change/100)
        elif size.lower()=="large":
            self.price=price+(price*Shirt.price_change*2/100)
        elif size.lower() == "xlarge":
            self.price=price+(price*Shirt.price_change*3/100)

    def ShowBook(self):
        print("Shirt ID:",self.sid)
        print("Shirt Name:",self.sname)
        print("Type:",self.type)
        print("Price:",self.price)
        print("Size:",self.size)

    def __del__(self):
        print("Shirt object destroyed")


s1 = Shirt(101,"Cotton Shirt","Formal",1000,"small")
s2 = Shirt(102,"Cotton Shirt","Formal",1000,"medium")
s3 = Shirt(103,"Cotton Shirt","Formal",1000,"large")
s4 = Shirt(104,"Cotton Shirt","Formal",1000,"xlarge")

s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()

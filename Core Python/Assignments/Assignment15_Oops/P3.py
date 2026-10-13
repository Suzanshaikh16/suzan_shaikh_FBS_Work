class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
    def __del__(self):
        print("Shirt object destroyed")

    def ShowShirt(self):
        print(f"Shirt Id={self.sid}\tName={self.sname}\tType={self.type}\tPrice={self.price}\tSize={self.size}")

s1 = Shirt(101, "Formal Shirt", "Formal", 800, "Large")
s1.ShowShirt()

s2 = Shirt()
s2.ShowShirt()
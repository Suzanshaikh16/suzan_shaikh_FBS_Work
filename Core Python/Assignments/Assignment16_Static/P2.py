
class Product:
    discount=10  

    def __init__(self,pid=0,pname="",price=0.0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def ApplyDiscount(self):
        self.price=self.price-(self.price*Product.discount/100)

    def ShowBook(self):
        print("Product ID:",self.pid)
        print("Product Name:",self.pname)
        print("Price:",self.price)
        print("Quantity:",self.quantity)

    def __del__(self):
        print("Product object destroyed")


p1 = Product()
p2 = Product(101,"Laptop",50000,2)

p2.ApplyDiscount()

p1.ShowBook()
p2.ShowBook()

print("Discount:",Product.discount,"%")

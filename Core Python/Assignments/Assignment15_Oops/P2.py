class Product:
    def __init__(self,pid=0,pname="",price="",quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
    def __del__(self):
        print("Product object destroyed")

    def ShowProduct(self):
        print(f'Product Id={self.pid}\tProduct Name={self.pname}\tPrice={self.price}\tQuantity={self.quantity}')  
p1=Product(101,'Laptop',5000,2)
p1.ShowProduct()  

p1=Product()
p1.ShowProduct()
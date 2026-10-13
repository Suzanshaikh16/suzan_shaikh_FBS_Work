class Book:
    def __init__(self,bid=0,bname="",price=0,author=""):
        self.bid= bid
        self.bname=bname
        self.price=price
        self.author=author
    def __del__(self):
        print("Book object destroyed")
    def ShowBook(self):
        print(f"Book Id={self.bid}\tBook Name={self.bname}\tPrice={self.price}\tAuthor={self.author}")
b1=Book(101,'The Secret',250,'Joseph')
b1.ShowBook()

b2=Book()
b2.ShowBook()
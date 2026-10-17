from Book import Book

books = {}

while True:
    print("\n1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        bid = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        price = float(input("Enter Price: "))
        author = input("Enter Author: ")

        books[bid] = Book(bid, name, price, author)
        print("Book Added Successfully")

    elif ch == 2:
        bid = int(input("Enter Book ID to delete: "))

        if bid in books:
            del books[bid]
            print("Book Deleted Successfully")
        else:
            print("Book Not Found")

    elif ch == 3:
        if len(books) == 0:
            print("No Books Available")
        else:
            for b in books.values():
                b.display()

    elif ch == 4:
        bid = int(input("Enter Book ID to search: "))

        if bid in books:
            books[bid].display()
        else:
            print("Book Not Found")

    elif ch == 5:
        break

    else:
        print("Invalid Choice")

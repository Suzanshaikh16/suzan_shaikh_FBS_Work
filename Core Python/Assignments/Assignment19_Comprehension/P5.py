s = input("Enter a string: ")

words=s.split()

for i in words:
    if len(i) < 5:
        print(i)
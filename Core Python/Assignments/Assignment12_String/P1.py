s = input("Enter a string: ")
new = ""
for ch in s:
    if ch=='a':
        new=new+'$'
    else:
        new=new+ch

print("String after replacement:", new)
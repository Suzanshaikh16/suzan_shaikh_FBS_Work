s=input("Enter a string: ")

if len(s)==1:
    new=s
else:
    new = s[len(s)-1]
    for i in range(1, len(s)-1):
        new=new+s[i]
    new=new+s[0]
print("New string:",new)
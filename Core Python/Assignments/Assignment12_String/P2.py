s=input("Enter a string: ")
n=int(input("Enter the index to remove: "))

new = ""

for i in range(len(s)):
    if i!=n:
        new=new+s[i]

print("String after removing character:",new)
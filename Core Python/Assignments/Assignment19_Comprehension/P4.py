s = input("Enter a string: ")

result = ""

for i in s:
    if i not in "aeiouAEIOU":
        result=result+i

print("String after removing vowels:",result)
s = input("Enter a string: ")

count=0

for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        count=count+1

print("Number of vowels:",count)
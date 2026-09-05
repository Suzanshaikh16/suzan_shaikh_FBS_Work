li=[10, 20, 10, 30, 10, 40, 20]
n = int(input("Enter a number: "))
count=0
for num in li:
    if num==n:
        count=count+1

if count>0:
    print("Element is present in the list")
    print("It is present", count, "times")
else:
    print("Element is not present in the list")
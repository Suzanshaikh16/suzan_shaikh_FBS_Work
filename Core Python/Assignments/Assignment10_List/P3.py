li = [10, 25, 5, 40, 15]
largest = li[0]
second = li[0]
for i in li:
    if (i>largest):
        second=largest
        largest=i
    elif (i>second and i!=largest):
        second=i

print("Second largest element:", second)
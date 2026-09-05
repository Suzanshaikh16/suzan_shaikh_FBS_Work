n = int(input("Enter number of elements: "))
li1 = []
for i in range(n):
    num = int(input("Enter element: "))
    li1.append(num)
even = []
odd = []
for i in li1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Original list:', li1)
print('Even elements:', even)
print('Odd elements:', odd)
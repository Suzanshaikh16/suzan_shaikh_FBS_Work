n =int(input('Enter n element: '))
li = []
even = []
odd = []
for i in range(n):
    e = int(input('Enter element: '))
    li.append(e)
for i in range(n):
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i])
print('Original list:',li)
print('Even list:',even)
print('Odd list:',odd)
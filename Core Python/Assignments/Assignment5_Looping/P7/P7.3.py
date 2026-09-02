n =int(input('Enter n number: '))
num = 1
sum = 0

for i in range(1,n+1):
    sum = sum+num
    num = num*2

print('Sum: ',sum)
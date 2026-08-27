#Armstrong number: A number where the sum of the powers of its digits equals the original number.

n =int(input('Enter a number: '))

temp = n
sum = 0

while(temp>0):
    d = temp%10
    sum = sum+d**3
    temp = temp//10
if(sum==n):
    print('Number is a Armstrong Number.')
else:
    print('Number is not a Armstrong Number.')


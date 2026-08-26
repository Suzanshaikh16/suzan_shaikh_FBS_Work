#the addition of factors of no. should be equal to no. is called perfect
n =int(input('Enter number: '))
p = 0
for i in range(1,n):
    if(n%i==0):
        p = p+i
if(p==n):
    print('Number is perfect.')
else:
    print('Number is not perfect.')
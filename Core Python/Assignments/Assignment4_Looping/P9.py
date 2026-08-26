n =int(input('Enter number: '))
s =int(input('Enter starting no. in range: '))
st =int(input('Enter stopping no. in range: '))

for i in range(s,st+1):
    if(i%n==0):
        print(i)
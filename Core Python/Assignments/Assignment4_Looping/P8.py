s =int(input('Enter starting no. in range: '))
st =int(input('Enter stopping no. in range: '))

for i in range(s,st+1):
    if(i%7==0 and i%5==0):
        print(i)
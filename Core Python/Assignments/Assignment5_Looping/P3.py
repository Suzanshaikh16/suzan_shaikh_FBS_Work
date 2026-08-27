n =int(input('Enter number of passengers: '))
t =int(input('Per ticket cost: '))
total = 0

for i in range(1, n + 1):
    a =int(input('Age of Passenger: '))
    if(a<12):
        ticket =t-(t*30/100)
    elif(a>59):
        ticket =t-(t*50/100)
    else:
        ticket = t
    total=total+ticket
print('Total amount: ',total)



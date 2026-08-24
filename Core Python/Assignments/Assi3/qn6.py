sp =int(input('Enter selling price: '))
cp =int(input('Enter cost price: '))

if(sp>cp):
    profit = sp-cp
    print('profit: ',profit)
elif(cp>sp):
    loss = cp-sp
    print('Loss: ',loss)
else:
    print('No profit no loss.')



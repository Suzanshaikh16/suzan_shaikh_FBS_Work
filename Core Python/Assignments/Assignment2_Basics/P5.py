c =int(input('Enter cost price of book: '))
d =float(input('Enter discount on book: '))

dprice = (c*d)/100
sprice = c-dprice
print(f'Selling price of book is {sprice}.')
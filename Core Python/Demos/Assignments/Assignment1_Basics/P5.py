P = int(input('enter priciple: '))
R = float(input('enter rate: '))
T = int(input('enter time: '))

cint = P *(1+(R/100))**T-P

print(cint)
print(f'simple interest is {cint}')
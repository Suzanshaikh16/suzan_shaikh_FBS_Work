num1 = int(input('enter a number1: '))
num2 = int(input('enter a number2: '))
num3 = int(input('enter a number3: '))

#num1x+num2x+num3=0
#num4 = num2**2 - 4*num1*num3

num4 = (num2**2) - 4*num1*num3

root1 = ((-num2 + num4**0.5)/(2*num1))
root2 = ((-num2 - num4**0.5)/(2*num1))

print(root1)
print(root2)

print(f'Roots of quadratic equation is {root1} and {root2}')


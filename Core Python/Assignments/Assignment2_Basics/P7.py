num =int(input('Enter number: '))

d1 = num//100
d2 = (num//10)%10
d3 = num%10

sum = d1+d2+d3
print(f'Sum of number is {sum}.')
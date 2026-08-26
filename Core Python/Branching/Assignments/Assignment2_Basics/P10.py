num =int(input('enter digit: '))

d1 = num//100
d2 = (num//10)%10
d3 = num%10
rev = d3 * 100 + d2 * 10 + d1
print(f'{rev}')

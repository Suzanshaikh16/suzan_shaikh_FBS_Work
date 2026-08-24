a =int(input('Enter angle1: '))
b =int(input('Enter angle2: '))
c =int(input('Enter angle3: '))

if(a==b and b==c):
    print('Triangle is equilateral.')
elif(a==b or b==c or c==a):
    print('Triangle is isosceles')
else:
    print('Triangle is scalene')







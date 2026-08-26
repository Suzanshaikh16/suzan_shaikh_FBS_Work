a =int(input('Enter marks of English: '))
b =int(input('Enter marks of Java: '))
c =int(input('Enter marks of Python: '))
d =int(input('Enter marks of Maths: '))
e =int(input('Enter marks of Science: '))

p = (a+b+c+d+e)/500*100

if(p>=80):
    print('Grade:Distinction')
elif(p>=70):
    print('Grade:First class')
elif(p>=50):
    print('Grade:Second class')
elif(p>=35):
    print('Pass')
else:
    print('Fail')


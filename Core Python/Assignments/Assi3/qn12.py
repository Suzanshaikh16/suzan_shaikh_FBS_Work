num =int(input('Enter a number: '))

d1 = num//100
d2 = (num//10)%10
d3 = num %10
if (d1==d3):
    print('Number is Palindrome.')
else:
    print('Number is not Palindrome.')
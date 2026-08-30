def odd(n):
    sum = 0
    for i in range(1,n+1,2):
        sum = sum+i
    return sum
n =int(input('Enter n: '))
c =odd(n)
print('Sum: ',c)
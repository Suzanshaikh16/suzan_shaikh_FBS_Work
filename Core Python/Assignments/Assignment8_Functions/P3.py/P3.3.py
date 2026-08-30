def power():
    n = int(input('Enter n: '))
    sum = 0
    for i in range(1,n+1):
        power = i**i
        sum = sum+power
    return sum
c = power()
print('Sum: ',c)

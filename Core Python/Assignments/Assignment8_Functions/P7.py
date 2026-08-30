def digits(n):
    sum = 0
    while (n>0):
        digit = n % 10
        sum = sum + digit
        n = n//10
    return sum
n = int(input('Enter n: '))
res =digits(n)
print('Series: ',res)
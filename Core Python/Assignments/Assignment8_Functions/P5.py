def prime(n):
    sum = 0
    for i in range(2,n+1):
        count = 0
        for j in range(1,i+1):
            if (i%j==0):
                count = count+1
        if count ==2:
            sum = sum+i
    return sum
n =int(input('Enter n: '))
res =prime(n)
print('Sum: ',res)
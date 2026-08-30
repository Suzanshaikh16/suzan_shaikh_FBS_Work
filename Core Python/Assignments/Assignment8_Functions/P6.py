def fibo(n):
    a =1
    b =1
    for i in range(n):
        c = a+b
        print(a,end=' ')
        a = b
        b = c
    return c
n = int(input('Enter n: '))
res =fibo(n)
print('Series: ',res)
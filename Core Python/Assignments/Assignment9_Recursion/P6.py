def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
num = int(input("Enter number of terms: "))

for i in range(num):
    print(fibo(i), end=" ")
def soS(n):
    if(n <= 0):
        return 0
    else:
        return n + soS(n-1)

num = int(input('enter number:'))
res = soS(num)
print(res)
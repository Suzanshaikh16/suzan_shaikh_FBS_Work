n=5
for i in range(1,n+1):
    for j in range(i,n+1):
        if i==1:
            print(j,end=' ')
        elif j==i:
            print(i,end=' ')
        elif j==n:
            print(5,end=' ')
        else:
            print(' ',end=' ')
    print()

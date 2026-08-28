for i in range(0,4):
    for j in range(0,3-i):
        print(' ',end=' ')
    for j in range(0,i+1):
        if(j==0 or j==i):
            print(1,end='   ')
        else:
            print(i,end='   ')
    print()

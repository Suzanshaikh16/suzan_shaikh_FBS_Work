for i in range(1,6):
    num = 1
    for j in range(1,6):
        if(i==j):
            print(j,end=' ')
        elif(j==num):
            print(1,end=' ')
        elif(i==5):
            print(j,end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,i+1):
        print(' ',end=' ')

    print()
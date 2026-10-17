n=int(input("Enter number of coins: "))
l=list(map(int, input("Enter coin numbers: ").split()))

for i in l:
    if l.count(i)%2!=0:
        print(i)
        break
# prime no.:-if no is divisible by 1 and itself is called prime no.s

for n in range(2,101):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            
            count = count+1
    if(count==2):
            print(n)
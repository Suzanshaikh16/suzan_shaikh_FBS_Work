start =int(input('Enter starting of range: '))
stop =int(input('Enter stopping of range: '))
for i in range(start,stop+1):
    temp =i
    sum =0
    while(temp>0):
        d = temp%10
        sum = sum+d**3
        temp = temp//10
    if(sum==i):
        print(i)


    


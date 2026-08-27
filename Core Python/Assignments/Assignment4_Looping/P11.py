 #sum of the factorials of its digits is equal to the original number is called strong no.

n =int(input('Enter number: '))

temp = n
sum = 0
while(temp>0):
    d = temp%10
    fact = 1
    for i in range(1,d+1):
        fact = fact*i

    sum = sum+fact
    temp = temp//10
if(sum==n):
    print('Number is a Strong number.')
else:
    print('Number is not a Strong number.')
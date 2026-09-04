def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
def armstrong_sum(n,digits):
    if n==0:
        return 0
    digit=n%10
    return digit**digits+armstrong_sum(n//10,digits)

num = int(input("Enter a number: "))
digits=count_digits(num)
sum=armstrong_sum(num,digits)
if sum==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
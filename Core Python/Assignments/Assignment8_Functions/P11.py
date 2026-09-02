def armstrong(n):
    original = n
    sum = 0
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10
    if sum == original:
        return True
    else:
        return False
n = int(input("Enter number: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
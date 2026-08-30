def palindrome(n):
    num = n
    rev = 0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if (num == rev):
        return True
    else:
        return False


n = int(input("Enter number: "))
if(palindrome(n)):
    print('Number is Palindrome')
else:
    print('Number is not Palindrome')


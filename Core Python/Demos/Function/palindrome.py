#wap to check the number is palindrome or not
#return true if palindrome & return false if not palindrome
def chkPalindrome(num):
    temp = num
    rev = 0
    while(temp>0):
        d = temp%10
        temp = temp// 10
        rev = rev*10+d
    if(num == rev):
        return True
    else:
        return False

n = int(input('Enter a number: '))
print(chkPalindrome(n))
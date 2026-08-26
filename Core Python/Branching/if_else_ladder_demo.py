num=int(input('enter a number: '))
if(num==0):
    print('The number is neutral')
elif(num>0):
        print(f'{num} is a positive no.')
else:
    print(f'{num} is a negative')
##less than 0 and greater than 250
num=int(input('enter a number: '))
if(num<=0):
     print('less than and equal to zero')
elif(num<50):
     print('1-50')
elif(num<70):
     print('51-70')
elif(num<100):
     print('71-100')
elif(num<150):
     print('101-150')
elif(num<250):
     print('151-250')
else:
     print('Greater than 250')
##by nested if else
num = int(input("Enter a number: "))

if num <= 0:
    print("Less than and equal to zero")
else:
    if num < 50:
        print("1-50")
    else:
        if num < 70:
            print("51-70")
        else:
            if num < 100:
                print("71-100")
            else:
                if num < 150:
                    print("101-150")
                else:
                    if num < 250:
                        print("151-250")
                    else:
                        print("Greater than 250")

print(10+20) #hardcoded values
#addition
num=6
num1=2
print(num+num1)
#concatenation
str1='abc'
str2='cde'
print(str1+str2)
#substraction
print(num-num1)
#multiplication
print(num*num1)
#division
print(num/num1)
#floor division
print(num//num1)
#modulus
print(num%num1)
#exponential
print(num**num1)

##program of addition
num1=int(input('enter number: '))
num2=int(input('enter number: '))
sum=num1+num2
print(sum)
print('Addition: ',sum)
#f-string
print(f'Addition of {num1}and addition of {num2} is {sum}')
##program of substraction
num1=int(input('enter a value: '))
num2=int(input('enter a value: '))
minus=num1-num2
print(minus)
print('substraction: ',minus)
##calculate simple interest
principle=int(input('enter a value'))
rate=float(input('enter a value'))
time=int(input('enter a value'))
sint=principle*rate*time/100
print('sint : ',sint)





num =int(input('Enter integer amount: '))

a = num//2000
b = num % 2000
c = b // 500
d = b % 500
e = d// 200
f = d% 200
g = f //100
h =f% 100
i = h //50
j = h% 50
k = j //20
l = j % 20
m = l//10
n = l% 10

total = a+c+e+g+i+k+m

print(f'Total no. of notes are {total}.')


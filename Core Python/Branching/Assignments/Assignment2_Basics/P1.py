a =int(input('time entered in hours: '))
b =int(input('time entered in min: '))
c =int(input('time entered in seconds: '))

s = c*1

m = b*60

h = a*3600

t = s+m+h

print(h)
print(m)
print(s)
print(f'Total seconds is {t}')
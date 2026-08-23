#pass:
for i in range(1,10):
    pass

#break:
for i in range(1,10):
    if(i==3):
        break
    print(i)

#continue:
for i in range(1,10):
    if(i==3):
        continue
    print(i)

#else:

for i in range(1,10):
    if(i==5):
        break
    print(i)
else:
    print('else executed')

for i in range(1,10):
    if(i==5):
        continue
    print(i)
else:
    print('else executed')
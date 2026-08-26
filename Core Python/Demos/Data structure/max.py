li = [45, 67, 23, 89, 56, 13, 10, 90]
max = li[0]

for ind in range(1,len(li)):
    if(li[ind] > max):
        max = li[ind]

print('Maximum:',max)

#wap to calculate second max element from list
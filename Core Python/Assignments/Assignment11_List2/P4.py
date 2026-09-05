li = [10,25,7,40,15]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]

print("Sorted list:",li)
print("Second largest:",li[-2])
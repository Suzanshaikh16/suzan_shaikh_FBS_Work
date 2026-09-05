li=[2, 4, 3, 5, 7, 8, 9]
val=10
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==val:
            print(li[i],li[j])
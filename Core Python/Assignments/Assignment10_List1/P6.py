li = [10, 20, 10, 30, 20, 40, 30]
unique = []
for i in li:
    found = 0
    for n in unique:
        if i==n:
            found=1
            break
    if found==0:
        unique=unique+[i]
print("List after removing duplicates:", unique)
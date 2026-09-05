li1 = [5, 2, 8]
li2 = [7, 1, 4]

merged = li1 + li2

for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            temp = merged[i]
            merged[i] = merged[j]
            merged[j] = temp


print("Merged and Sorted List:", merged)
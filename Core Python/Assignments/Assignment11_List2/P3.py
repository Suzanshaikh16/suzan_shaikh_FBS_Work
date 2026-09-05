li = [[10, 25], [20, 5], [30, 15], [40, 35]]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:
            li[i], li[j] = li[j], li[i]

print("Sorted list:", li)
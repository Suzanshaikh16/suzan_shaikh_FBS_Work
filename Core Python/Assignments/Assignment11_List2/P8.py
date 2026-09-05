num = 1
for i in range(10):
    row = []
    for j in range(10):
        row.append(num)
        num = num+1
    if i%2!=0:
        row.reverse()
    print(row)
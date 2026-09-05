li = [10, 30, 5, 60, 45]
max=li[0]
min=li[0]
for num in li:
    if num > max:
        max = num
    if num < min:
        min = num
print('Maximum no. is ',max)
print('Minimum no. is ',min)

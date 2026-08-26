def add(*data):
    sum = 0 #take one variable called sum and start adding values
    for val in data:
        sum+=val
    return sum

res = add(10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(res)
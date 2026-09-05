n = int(input("Enter number of elements: "))
numbers = []
squares = []
cubes = []
for i in range(n):
    n = int(input("Enter number: "))
    numbers.append(n)
    squares.append(n*n)
    cubes.append(n*n*n)
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
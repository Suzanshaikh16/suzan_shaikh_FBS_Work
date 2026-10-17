n = 22          
rows = 10       
print("*" * n)
for i in range(rows):
    print(" " * (n - 2 * i) + "*")
print("*" * n)
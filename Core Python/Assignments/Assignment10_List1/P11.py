li1 = [10, 15, 20, 30, 40, 60]
m = int(input("Enter m: "))
n = int(input("Enter n: "))
print("Numbers divisible by both m and n:")
for i in li1:
    if i%m==0 and i%n==0:
        print(i)
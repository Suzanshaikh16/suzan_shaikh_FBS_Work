def my_range(start, stop, step):
    while start < stop:
        yield start
        start = start + step

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

for i in my_range(start, stop, step):
    print(i)
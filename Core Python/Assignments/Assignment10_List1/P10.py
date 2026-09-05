li1 = [10, 20, 10, 30, 10, 40]
num = int(input("Enter element to remove: "))
li2 = []
for i in li1:
    if i!=num:
        li2.append(i)
print("Original list:", li1)
print("List after removing all occurrences:", li2)
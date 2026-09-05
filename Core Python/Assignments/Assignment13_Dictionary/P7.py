dict1={1: 'Python', 2: 'Java', 3: 'cpp'}

key=int(input("Enter key to remove: "))

if key in dict1:
    del dict1[key]
    print("Updated dictionary:", dict1)
else:
    print("Key does not exist")
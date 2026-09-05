dict1={1: 'Suzan', 2: 'Shaikh', 3: 'Sayyed'}

key=int(input("Enter key to search: "))

if key in dict1:
    print('Key exists in dictionary')
else:
    print('Key does not exist in dictionary')
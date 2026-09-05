str1 = input("Enter a string: ")
words = str1.split()
dict1 = {}
for word in words:
    if word in dict1:
        dict1[word]=dict1[word]+1
    else:
        dict1[word]=1

print(dict1)
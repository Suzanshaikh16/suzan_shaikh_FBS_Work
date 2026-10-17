s = input("Enter a sentence: ")

words = s.split()

d = {i: len(i) for i in words}

print(d)
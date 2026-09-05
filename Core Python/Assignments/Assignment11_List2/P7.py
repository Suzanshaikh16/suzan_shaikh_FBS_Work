li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]
intersection = []
for i in li1:
    if i in li2:
        intersection.append(i)

print("Intersection of two lists:", intersection)
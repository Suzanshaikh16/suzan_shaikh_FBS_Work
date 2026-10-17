li1=[1, 2, 3, 4]
li2=[3, 4, 5, 6]
li3=[]

for i in li1:
    if i not in li3:
        li3.append(i)

for i in li2:
    if i not in li3:
        li3.append(i)

print("Union:", li3)
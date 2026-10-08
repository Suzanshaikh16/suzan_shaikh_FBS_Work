f=None
try:
    f=open("abc.txt","r")
    data=f.read()
except Exception as e:
    print(e)
else:
    print(data)
# finally:
#     f.close()
print("I am in outside ABc")

f=open("abc.txt",'w')
f.write("MI Won 5 cups\nRCB WON The 2 cups")
f.writelines(["\nI am good in coding","\nI am not good in Python"])

f=open("abc.txt",'a')
with open("abc.txt",'a')as f:
    f.write("\nKKR Won 3 cups")
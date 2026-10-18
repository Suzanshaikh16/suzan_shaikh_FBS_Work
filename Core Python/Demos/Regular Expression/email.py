import re
email=input("Enter the mail to check")
pat=r"^[a-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
res=re.search(pat,email)
if res:
    print("Pattern found")
else:
    print("Pattern is not found")
s = input("Enter a string: ")
word = ""
large = ""
count = 0
large_count = 0

for ch in s:
    if ch!=' ':
        word=word+ch
        count=count+1
    else:
        if count>large_count:
            large=word
            large_count=count

        word=""
        count=0

if count>large_count:
    large=word

print("Larger string:",large)
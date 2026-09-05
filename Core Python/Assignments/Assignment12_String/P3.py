s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1)!=len(s2):
    print("Strings are not anagrams")
else:
    count=0

    for ch in s1:
        if ch in s2:
            count=count+1

    if count==len(s1):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
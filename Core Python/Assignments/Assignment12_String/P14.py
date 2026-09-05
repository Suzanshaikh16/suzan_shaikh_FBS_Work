s = input("Enter a string: ")
words=s.split()
visited=[]
for word in words:
    if word not in visited:
        count=0
        for w in words:
            if w==word:
                count=count+1

        print(word, ":",count)
        visited.append(word)
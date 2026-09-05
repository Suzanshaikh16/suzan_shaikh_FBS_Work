strg=['python', 'java', 'cpp', 'eng', 'java', 'python']

unique_words=set(strg)

for word in unique_words:
    count=0

    for item in strg:
        if item==word:
            count+=1

    print(word, ':', count)
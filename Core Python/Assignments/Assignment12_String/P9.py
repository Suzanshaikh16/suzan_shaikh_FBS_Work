s = input("Enter a string: ")

characters = 0
words = 0
in_word = False

for ch in s:
    characters = characters + 1

    if ch != ' ' and in_word == False:
        words = words + 1
        in_word = True

    elif ch == ' ':
        in_word = False

print("Number of words:", words)
print("Number of characters:", characters)
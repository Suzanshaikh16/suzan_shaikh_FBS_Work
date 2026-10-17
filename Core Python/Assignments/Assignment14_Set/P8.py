
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = {}

for word in words:
    key = "".join(sorted(word))

    if key not in result:
        result[key] = []

    result[key].append(word)

print("Anagram groups:")

for group in result.values():
    print(group)

sentence = input().split()

for word in sentence:
    for j in range(0, len(word)):
        if word[j] == ":":
            result = word[j:j + 2]
            print(result)

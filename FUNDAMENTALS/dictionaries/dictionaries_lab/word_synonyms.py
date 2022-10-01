count_of_words = int(input())

all_synonyms = {}

for words in range(0, count_of_words):
    word = input()
    synonym = input()
    if word not in all_synonyms:
        all_synonyms[word] = []
        all_synonyms[word].append(synonym)
    else:
        all_synonyms[word].append(synonym)


for key, value in all_synonyms.items():
    print(f"{key} - {', '.join(value)}")

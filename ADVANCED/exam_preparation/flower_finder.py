from collections import deque


def check_length(index):
    result = False
    if (searched[index]) == "":
        result = True
        print(f"Word found: {searched_words[index]}")

    return result


vowels = deque(input().split())
consonants = input().split()

searched_words = ["rose", "tulip", "lotus", "daffodil"]

searched = ["rose", "tulip", "lotus", "daffodil"]
word_found = False

while consonants and vowels:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for i in range(len(searched)):
        if current_consonant in searched[i]:
            searched[i] = searched[i].replace(current_consonant, "")
        if check_length(i):
            word_found = True
            break
        if current_vowel in searched[i]:
            searched[i] = searched[i].replace(current_vowel, "")
        if check_length(i):
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

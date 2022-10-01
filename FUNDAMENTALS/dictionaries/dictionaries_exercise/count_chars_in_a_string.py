word = input()

all_letters = {}

if " " in word:
    word = word.split(" ")
    for current_word in word:
        for letter in range(len(current_word)):
            if current_word[letter] not in all_letters:
                all_letters[current_word[letter]] = 1
            else:
                all_letters[current_word[letter]] += 1

else:
    for letter in range(len(word)):
        if word[letter] not in all_letters:
            all_letters[word[letter]] = 1
        else:
            all_letters[word[letter]] += 1


for key, value in all_letters.items():
    print(f"{key} -> {value}")
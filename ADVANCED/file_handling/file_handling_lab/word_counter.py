import re

word_dict = {}
pattern = r"[a-zA-Z']+"

with open("../files/words.txt", "r") as file:
    words = file.readline().split()

for word in words:
    word_dict[word] = 0

with open("../files/input.txt", "r") as file_information:
    sentences = file_information.readlines()

for current_sentence in range(len(sentences)):
    split_sentence = re.findall(pattern, sentences[current_sentence].lower())
    for current_key in word_dict:
        for current_word in split_sentence:
            if current_key == current_word:
                word_dict[current_key] += 1

sorted_dict = sorted(word_dict.items(), key=lambda x: -x[1])

with open("../files/output.txt", "w") as new_file:
    for word, count in sorted_dict:
        new_file.write(f"{word} - {count}\n")


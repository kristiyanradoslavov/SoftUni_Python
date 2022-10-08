from string import punctuation

with open("text.txt", "r") as file_to_read:
    all_sentences = file_to_read.readlines()

for i in range(len(all_sentences)):
    current_sentence = all_sentences[i].strip()
    current_letters = 0
    current_punctuations = 0

    for j in range(len(all_sentences[i])):
        letter = all_sentences[i][j]
        if letter.isalpha():
            current_letters += 1
        elif letter in punctuation:
            current_punctuations += 1

    with open("output.txt", "a") as new_file:
        new_file.write(f"Line {i + 1}: {current_sentence} ({current_letters})({current_punctuations})\n")

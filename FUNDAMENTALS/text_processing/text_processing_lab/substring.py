word_to_remove = input()
second_word = input()

while word_to_remove in second_word:
    second_word = second_word.replace(word_to_remove, "")

print(second_word)

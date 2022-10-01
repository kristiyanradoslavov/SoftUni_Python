input_words = input().split()

for i in input_words:
    final_word = i * len(i)
    print(final_word, end = "")

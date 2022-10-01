import re

sentence = input().lower()
word_to_search = input().lower()

current_pattern = fr"\b{word_to_search}\b"

result = re.findall(current_pattern, sentence)

print(len(result))
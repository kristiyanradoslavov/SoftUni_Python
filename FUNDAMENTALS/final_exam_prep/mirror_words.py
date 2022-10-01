import re

word_text = input()
pattern = r"(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

result = re.finditer(pattern, word_text)

valid_pairs = 0
valid_dict = {}
for i in result:
    valid_pairs += 1
    first_word = i.group(2)
    second_word = i.group(3)
    reversed_second = "".join(reversed(second_word))
    if first_word == reversed_second:
        valid_dict[first_word] = second_word

if valid_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{valid_pairs} word pairs found!")

if valid_dict:
    print("The mirror words are:")
    for index, value in enumerate(valid_dict):
        if index < len(valid_dict) - 1:
            print(f"{value} <=> {valid_dict[value]}, ", end="")
        else:
            print(f"{value} <=> {valid_dict[value]}")
else:
    print("No mirror words!")

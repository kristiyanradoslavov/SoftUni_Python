import re

sentence = input()

current_pattern = r"\b_([A-Za-z0-9]+)\b"

result = re.findall(current_pattern, sentence)

# for index, char in enumerate(result):
#     if index != len(result) - 1:
#         print(f"{char[1]}", end=",")
#     else:
#         print(f"{char[1]}")

print("".join(result))
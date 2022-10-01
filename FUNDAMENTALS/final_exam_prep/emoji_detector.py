import re


def find_numbers(txt):
    pattern = r"\d"
    all_digits = re.findall(pattern, txt)
    current_result = int(all_digits[0])
    for num in range(0, len(all_digits) - 1):
        result = int(current_result) * int(all_digits[num + 1])
        current_result = result
    return current_result


text = input()

threshold_number = find_numbers(text)

valid_emoji_pattern = r"(\:{2}|\*{2})([A-Z]{1}[a-z]{2,})\1"

valid_emoji = re.finditer(valid_emoji_pattern, text)
valid_emoji_length = re.findall(valid_emoji_pattern, text)

print(f"Cool threshold: {threshold_number}")
print(f"{len(valid_emoji_length)} emojis found in the text. The cool ones are:")

for emoji in valid_emoji:
    coolness = 0
    for letter in range(0, len(emoji.group(2))):
        coolness += ord(emoji.group(2)[letter])

    if coolness >= threshold_number:
        print(emoji.group())
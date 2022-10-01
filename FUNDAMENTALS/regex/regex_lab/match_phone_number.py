import re

phone_numbers = input()

current_pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

result = re.findall(current_pattern, phone_numbers)

print(", ".join(result))
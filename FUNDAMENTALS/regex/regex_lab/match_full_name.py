import re

current_name = input()

current_regex = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

final_result = re.findall(current_regex, current_name)

print(" ".join(final_result))
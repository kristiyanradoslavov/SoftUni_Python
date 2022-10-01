import re

dates = input()

current_pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"

result = re.findall(current_pattern, dates)


for position in result:
    print(f"Day: {position[0]}, Month: {position[2]}, Year: {position[3]}")
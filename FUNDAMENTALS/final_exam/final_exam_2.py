import re

number_of_inputs = int(input())
pattern = r"\|([A-Z]{4,})\|\:\#([A-Za-z]+\s[A-Za-z]+)\#"

for i in range(number_of_inputs):
    current_input = input()
    result = re.findall(pattern, current_input)
    if result:
        for res in result:
            strength = len(res[0])
            armor = len(res[1])
            print(f"{res[0]}, The {res[1]}")
            print(f">> Strength: {strength}")
            print(f">> Armor: {armor}")
    else:
        print("Access denied!")
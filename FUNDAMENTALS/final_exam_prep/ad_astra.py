import re

food_information = input()

pattern = r"(\#|\|)([a-zA-Z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"
calories_pattern = r"(\#|\|)(\d+)\1"

result = re.finditer(pattern, food_information)

total_calories = 0
for first in result:
    current_group = str(first.group())
    calories_result = re.finditer(calories_pattern, current_group)
    for i in calories_result:
        calories = i.group(2)
        total_calories += int(calories)

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")

result_2 = re.finditer(pattern, food_information)

for res in result_2:
    print(f"Item: {res.group(2)}, Best before: {res.group(3)}, Nutrition: {res.group(4)}")
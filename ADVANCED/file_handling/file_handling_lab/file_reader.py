
final_result = 0

with open("numbers.txt", "r") as file:
    result = file.readlines()

for i in result:
    result = i.strip()
    final_result += int(result)

print(final_result)

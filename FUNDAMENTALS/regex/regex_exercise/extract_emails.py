import re

current_pattern = r"((?<=\s)[a-z0-9]+[\.\-\_]?[a-z0-9]+\@([a-zA-Z]+[\-]?[a-zA-Z]+)(\.[a-z]+)+\b)"

current_input = input()

result = re.findall(current_pattern, current_input)

for i in result:
    print(i[0])

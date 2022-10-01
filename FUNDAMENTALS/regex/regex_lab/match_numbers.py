import re

pattern = r"((^|(?<=\s))\-?([0]|[1-9][0-9]*))(\.\d+)?($|(?=\s))"

curr_input = input()

result = re.finditer(pattern, curr_input)

for i in result:
    print(i.group(),end=" ")
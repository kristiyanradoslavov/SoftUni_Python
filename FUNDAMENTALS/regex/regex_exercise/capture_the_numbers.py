import re
current_input = input()
current_pattern = r"\d+"


while True:
    if current_input:
        result = re.findall(current_pattern, current_input)
        if result:
            print(" ".join(result), end=" ")
    else:
        break

    current_input = input()





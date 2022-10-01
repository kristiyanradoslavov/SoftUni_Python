first_input = input()

final_string = ""

for i in first_input:
    if i == " ":
        final_string += "#"
    else:
        current_num = ord(i)
        final_string += chr(current_num + 3)

print(final_string)
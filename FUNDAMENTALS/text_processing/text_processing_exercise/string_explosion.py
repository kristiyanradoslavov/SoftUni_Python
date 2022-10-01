incoming_string = input()

strength = 0

final_string = ""

for index in range(len(incoming_string)):
    if incoming_string[index] != ">" and strength > 0:
        strength -= 1
    elif incoming_string[index] == ">":
        strength += int(incoming_string[index + 1])
        final_string += incoming_string[index]
    else:
        final_string += incoming_string[index]

print(final_string)
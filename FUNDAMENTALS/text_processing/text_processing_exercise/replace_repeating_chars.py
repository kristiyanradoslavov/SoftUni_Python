starting_input = input()

final_string = starting_input
list_string = []
current_index = 0

list_string.append(starting_input[0])

for i in range(1, len(starting_input)):
    if list_string[current_index] != starting_input[i]:
        list_string.append(starting_input[i])
        current_index += 1

print("".join(list_string))
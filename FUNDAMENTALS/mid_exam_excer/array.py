numbers_array = list(map(int, input().split(" ")))

command = input()

while command != "end":
    input_command = command.split(" ")
    if input_command[0] == "swap":
        first_index = int(input_command[1])
        second_index = int(input_command[2])
        numbers_array[first_index], numbers_array[second_index] = numbers_array[second_index],numbers_array[first_index]
    elif input_command[0] == "multiply":
        first_index = int(input_command[1])
        second_index = int(input_command[2])
        numbers_array[first_index] = numbers_array[first_index] * numbers_array[second_index]
    elif input_command[0] == "decrease":
        numbers_array = list(map(lambda a: a - 1, numbers_array))

    command = input()

print(', '.join(str(a) for a in numbers_array))

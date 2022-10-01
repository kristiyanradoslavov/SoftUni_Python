sequence_of_targets = list(map(int, input().split(" ")))
command = input()

while command != "End":
    current_command = command.split(" ")
    if current_command[0] == "Shoot":
        index = int(current_command[1])
        power = int(current_command[2])
        if len(sequence_of_targets) - 1 >= index >= 0:
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)
    elif current_command[0] == "Add":
        index = int(current_command[1])
        value = int(current_command[2])
        if len(sequence_of_targets) - 1 >= index >= 0:
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif current_command[0] == "Strike":
        index = int(current_command[1])
        radius = int(current_command[2])
        low_radius = index - radius
        up_radius = index + radius
        wrong_input = True
        if len(sequence_of_targets) - 1 >= index >= 0:
            if len(sequence_of_targets) - 1 >= low_radius >= 0:
                if len(sequence_of_targets) - 1 >= up_radius >= 0:
                    sequence_of_targets[index] = 0
                    if radius > 0:
                        sequence_of_targets[up_radius] = 0
                        sequence_of_targets[low_radius] = 0
                        wrong_input = False
        if wrong_input:
            print("Strike missed!")
    command = input()

final_result = filter(lambda a: a != 0, sequence_of_targets)

print('|'.join(str(a) for a in final_result))
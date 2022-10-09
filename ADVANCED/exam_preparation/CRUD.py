def command_init_value(command, direction, value):
    new_row_pos = row_pos
    new_col_pos = col_pos
    row, col = [
        row_pos + directions_dict[direction][0],
        col_pos + directions_dict[direction][1]
    ]
    if 0 <= row < 6 and 0 <= col < 6:
        new_row_pos += directions_dict[direction][0]
        new_col_pos += directions_dict[direction][1]
        if command == "Create":
            if matrix[row][col] == ".":
                matrix[row][col] = value

        elif command == "Update":
            if matrix[row][col] != ".":
                matrix[row][col] = value
    return new_row_pos, new_col_pos


def command_init_no_value(command, direction):
    new_row_pos = row_pos
    new_col_pos = col_pos
    row, col = [
        row_pos + directions_dict[direction][0],
        col_pos + directions_dict[direction][1]
    ]
    if 0 <= row < 6 and 0 <= col < 6:
        new_row_pos += directions_dict[direction][0]
        new_col_pos += directions_dict[direction][1]
        if command == "Delete":
            if matrix[row][col].isdigit() or matrix[row][col].isalpha():
                matrix[row][col] = "."

        elif command == "Read":
            if matrix[row][col].isdigit() or matrix[row][col].isalpha():
                print(matrix[row][col])
    return new_row_pos, new_col_pos


matrix = [input().split() for x in range(6)]
initial_position = input().split(", ")

row_pos = int("".join([x for x in initial_position[0] if x.isdigit()]))
col_pos = int("".join([x for x in initial_position[1] if x.isdigit()]))

directions_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()

while command != "Stop":
    current_command = command.split(", ")
    key_command = current_command[0]

    if key_command == "Create" or key_command == "Update":
        direction = current_command[1]
        new_value = current_command[2]
        row_pos, col_pos = command_init_value(key_command, direction, new_value)

    elif key_command == "Delete" or key_command == "Read":
        direction = current_command[1]
        row_pos, col_pos = command_init_no_value(key_command, direction)

    command = input()

for i in range(6):
    print(*matrix[i])
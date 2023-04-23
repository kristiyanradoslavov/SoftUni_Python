def create_com(com):
    _com, direction, value = com
    n_row, n_col = directions[direction]
    new_row, new_col = [
        row + n_row,
        col + n_col
    ]

    if matrix[new_row][new_col] == ".":
        matrix[new_row][new_col] = value

    return new_row, new_col


def update_com(com):
    _com, direction, value = com
    n_row, n_col = directions[direction]
    new_row, new_col = [
        row + n_row,
        col + n_col
    ]

    if matrix[new_row][new_col] != ".":
        matrix[new_row][new_col] = value

    return new_row, new_col


def delete_com(com):
    _com, direction = com
    n_row, n_col = directions[direction]
    new_row, new_col = [
        row + n_row,
        col + n_col
    ]

    if matrix[new_row][new_col] != ".":
        matrix[new_row][new_col] = "."

    return new_row, new_col


def read_com(com):
    _com, direction = com
    n_row, n_col = directions[direction]
    new_row, new_col = [
        row + n_row,
        col + n_col
    ]

    if matrix[new_row][new_col] != ".":
        print(matrix[new_row][new_col])

    return new_row, new_col


dimensions = 6

matrix = [input().split() for r in range(dimensions)]

first_pos = input()

row, col = [int(x) for x in first_pos if x.isdigit()]

commands = {
    "Create": create_com,
    "Update": update_com,
    "Delete": delete_com,
    "Read": read_com,
}

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

current_command = input()

while current_command != "Stop":
    command_info = current_command.split(", ")
    key_command = command_info[0]
    row, col = commands[key_command](command_info)

    current_command = input()

for current_row in matrix:
    print(" ".join(current_row))
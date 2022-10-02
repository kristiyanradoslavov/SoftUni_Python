matrix = []

targets = 0
shot_targets = []
my_position = []

for row in range(5):
    current_col = input().split()
    if "A" in current_col:
        my_position = [row, current_col.index("A")]

    for j in current_col:
        if j == "x":
            targets += 1

    matrix.append(current_col)

starting_number_of_targets = targets
move_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

count_of_targets = int(input())

for i in range(count_of_targets):
    if not targets:
        break
    current_command = input().split()
    key_command = current_command[0]

    if key_command == "move":  # very unclear in the description
        direction_to_move = current_command[1]
        steps = int(current_command[2])
        starting_position = my_position
        row, col = [
            my_position[0] + move_directions[direction_to_move][0] * steps,
            my_position[1] + move_directions[direction_to_move][1] * steps
        ]
        if 0 <= row < 5 and 0 <= col < 5:
            if matrix[row][col] == ".":
                my_position[0], my_position[1] = row, col
            else:
                my_position = starting_position
        else:
            my_position = starting_position

    elif key_command == "shoot":
        shoot_direction = current_command[1]
        direction_row, direction_col = [
            my_position[0] + move_directions[shoot_direction][0],
            my_position[1] + move_directions[shoot_direction][1]
        ]
        while True:
            if 0 <= direction_row < 5 and 0 <= direction_col < 5:
                if matrix[direction_row][direction_col] == "x":
                    shot_targets.append([direction_row, direction_col])
                    targets -= 1
                    matrix[direction_row][direction_col] = "."
                    break
                else:
                    direction_row += move_directions[shoot_direction][0]
                    direction_col += move_directions[shoot_direction][1]
            else:
                break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {starting_number_of_targets} targets hit.")

if shot_targets:
    for i in shot_targets:
        print(i)

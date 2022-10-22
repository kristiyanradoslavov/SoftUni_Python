size = int(input())
racing_number = input()

matrix = []
tunel_coordinates = []

for i in range(size):
    current_row = input().split()
    for j in current_row:
        if j == "T":
            tunel_coordinates.append((i, current_row.index("T")))
    matrix.append(current_row)

car_row, car_col = 0, 0

directions_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

total_distance = 0
car_finished = False

command = input()

while command != "End":
    current_command = command
    new_row, new_col = directions_dict[current_command][0] + car_row, directions_dict[current_command][1] + car_col

    if matrix[new_row][new_col] == "T":
        if (new_row, new_col) == tunel_coordinates[0]:
            car_row, car_col = tunel_coordinates[1]
        else:
            car_row, car_col = tunel_coordinates[0]

        first_tunel_row, first_tunel_col = tunel_coordinates[0][0], tunel_coordinates[0][1]
        second_tunel_row, second_tunel_col = tunel_coordinates[1][0], tunel_coordinates[1][1]
        matrix[first_tunel_row][first_tunel_col] = "."
        matrix[second_tunel_row][second_tunel_col] = "."
        total_distance += 30

    elif matrix[new_row][new_col] == "F":
        car_finished = True
        total_distance += 10
        car_row, car_col = new_row, new_col
        break

    else:
        total_distance += 10
        car_row, car_col = new_row, new_col

    command = input()


matrix[car_row][car_col] = "C"

if car_finished:
    print(f"Racing car {racing_number} finished the stage!")

else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_distance} km.")

for i in matrix:
    print(''.join(i))
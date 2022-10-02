number_of_presents = int(input())
size = int(input())

matrix = []
good_kids_count = 0
santa_locations = []
presents_given = 0

for i in range(size):
    current_line = input().split()
    if "S" in current_line:
        santa_locations = [i, current_line.index("S")]
    for j in current_line:
        if j == "V":
            good_kids_count += 1
    matrix.append(current_line)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

starting_good_kids = good_kids_count
command = input()
current_cookie_cell = []

while command != "Christmas morning":
    direction_to_move = command
    if number_of_presents == 0:
        break
    row, col = [
        santa_locations[0] + directions[direction_to_move][0],
        santa_locations[1] + directions[direction_to_move][1],
    ]

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "V":
            number_of_presents -= 1
            good_kids_count -= 1
            presents_given += 1
        elif matrix[row][col] == "C":
            current_cookie_cell = [row, col]
            for key, value in directions.items():
                r, c = [
                    row + directions[key][0],
                    col + directions[key][1]
                ]
                if 0 <= r < size and 0 <= c < size:
                    if matrix[r][c] == "V":
                        number_of_presents -= 1
                        good_kids_count -= 1
                        presents_given += 1
                    elif matrix[r][c] == "X":
                        number_of_presents -= 1
                        presents_given += 1

                    matrix[r][c] = "-"

        matrix[santa_locations[0]][santa_locations[1]] = "-"
        santa_locations = [row, col]
        matrix[row][col] = "S"

    if number_of_presents == 0:
        break
    command = input()


if number_of_presents == 0 and good_kids_count > 0:
    print("Santa ran out of presents!")

for row in range(size):
    print(*matrix[row], sep=" ")

if good_kids_count > 0:
    print(f"No presents for {good_kids_count} nice kid/s.")
else:
    print(f"Good job, Santa! {starting_good_kids} happy nice kid/s.")
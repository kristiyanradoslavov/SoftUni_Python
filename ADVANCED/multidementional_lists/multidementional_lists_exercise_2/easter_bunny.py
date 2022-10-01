size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_amount_of_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()

    if "B" in line:
        bunny_pos = [row, line.index("B")]
    matrix.append(line)

for key, value in directions.items():
    current_row, current_col = [
        bunny_pos[0] + value[0],
        bunny_pos[1] + value[1]
    ]
    total_eggs = 0
    current_path = []

    while 0 <= current_row < size and 0 <= current_col < size:
        if matrix[current_row][current_col] == "X":
            break

        total_eggs += int(matrix[current_row][current_col])
        current_path.append([current_row, current_col])

        current_row += value[0]
        current_col += value[1]

    if total_eggs >= max_amount_of_eggs:
        max_amount_of_eggs = total_eggs
        best_direction = key
        best_path = current_path

print(best_direction)
print(*best_path, sep="\n")
print(max_amount_of_eggs)

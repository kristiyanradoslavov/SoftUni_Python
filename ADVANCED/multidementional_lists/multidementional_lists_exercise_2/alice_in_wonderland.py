matrix_size = int(input())

matrix = [input().split() for x in range(matrix_size)]

bunny_col = 0
bunny_row = 0

for i in range(matrix_size):
    for j in range(matrix_size):
        if matrix[i][j] == "B":
            bunny_row = i
            bunny_col = j

directions = {
    "up": (bunny_row - 1, -1, -1),
    "down": (bunny_row + 1, matrix_size),
    "left": (bunny_col - 1, -1, -1),
    "right": (bunny_col + 1, matrix_size),
}

max_amount_of_eggs = 0
best_direction = None
best_path = []

for key, value in directions.items():
    total_eggs = 0
    current_path = []
    if key == "right" or key == "left":
        for col in range(*value):
            current_position = matrix[bunny_row][col]
            if current_position == "X":
                break
            else:
                total_eggs += int(current_position)
                current_path.append([bunny_row, col])
    elif key == "up" or key == "down":
        for row in range(*value):
            current_position = matrix[row][bunny_col]
            if current_position == "X":
                break
            else:
                total_eggs += int(current_position)
                current_path.append([row, bunny_col])

    if total_eggs >= max_amount_of_eggs:
        max_amount_of_eggs = total_eggs
        best_direction = key
        best_path = current_path

if best_direction:
    print(best_direction)
for i in best_path:
    print(i)
if max_amount_of_eggs:
    print(max_amount_of_eggs)

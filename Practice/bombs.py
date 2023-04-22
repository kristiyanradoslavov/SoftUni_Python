def print_matrix():
    for cur_row in matrix:
        print(" ".join(list(map(str, cur_row))))


rows = int(input())

matrix = [list(map(int, input().split())) for r in range(rows)]

coordinates_input = input().split()

coordinates = {}
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "u_left": [-1, -1],
    "u_right": [-1, 1],
    "d_left": [1, -1],
    "d_right": [1, 1]
}


for current_coordinates in range(len(coordinates_input)):
    row, col = list(map(int, coordinates_input[current_coordinates].split(",")))
    coordinates[current_coordinates] = [row, col]

for current_bomb in coordinates.values():

    row, col = current_bomb
    bomb_element = matrix[row][col]

    if bomb_element > 0:
        for current_direction in directions.values():
            r, c = current_direction
            new_row, new_col = [
                row + r,
                col + c
            ]
            if (new_row >= len(matrix) or new_row < 0) or (new_col >= len(matrix[new_row]) or new_col < 0):
                continue

            if matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= bomb_element

            matrix[row][col] = 0

alive_cells = [matrix[c_row][c_col] for c_row in range(len(matrix)) for c_col in range(len(matrix[c_row]))
               if matrix[c_row][c_col] > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
print_matrix()

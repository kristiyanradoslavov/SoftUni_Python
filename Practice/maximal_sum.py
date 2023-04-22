rows, cols = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for c in range(rows)]

max_sum = 0
max_matrix = []

for current_row in range(len(matrix) - 2):
    for current_col in range(len(matrix[current_row]) - 2):
        current_sum = 0
        current_sum += sum(matrix[current_row][current_col:current_col + 3])
        current_sum += sum(matrix[current_row + 1][current_col:current_col + 3])
        current_sum += sum(matrix[current_row + 2][current_col:current_col + 3])
        if current_sum >= max_sum:
            max_sum = current_sum
            max_matrix = [
                matrix[current_row][current_col:current_col + 3],
                matrix[current_row + 1][current_col:current_col + 3],
                matrix[current_row + 2][current_col:current_col + 3],
            ]

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(*row)

rows, cols = list(map(int, input().split()))

matrix = []

for row in range(rows):
    col = input().split()
    matrix.append(col)

total_matches = 0

for current_row in range(len(matrix)):
    matching_symbol = ""

    for current_col in range(len(matrix[current_row])):
        if current_col < len(matrix[current_row]) - 1 and current_row < len(matrix) - 1:
            if matrix[current_row][current_col] == matrix[current_row][current_col + 1]:
                matching_symbol = matrix[current_row][current_col]
                if matrix[current_row + 1][current_col] == matrix[current_row + 1][current_col + 1]:
                    next_match = matrix[current_row + 1][current_col]
                    if matching_symbol == next_match:
                        total_matches += 1

print(total_matches)
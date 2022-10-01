rows, cols = [int(x) for x in input().split()]

matrix = [list(map(int, input().split())) for x in range(rows)]

max_matrix = []
max_sum = 0

for i in range(len(matrix) - 2):
    for j in range(len(matrix[i]) - 2):
        first_row = matrix[i][j:j + 3]
        second_row = matrix[i + 1][j:j + 3]
        third_row = matrix[i + 2][j:j + 3]
        final_result = first_row + second_row + third_row
        current_sum = sum(final_result)
        if current_sum >= max_sum:
            max_matrix.clear()
            max_sum = current_sum
            max_matrix.append(first_row)
            max_matrix.append(second_row)
            max_matrix.append(third_row)

print(f"Sum = {max_sum}")
for i in range(len(max_matrix)):
    for j in range(len(max_matrix[i])):
        if j == len(max_matrix[i]) - 1:
            print(max_matrix[i][j])
        else:
            print(max_matrix[i][j], end=" ")

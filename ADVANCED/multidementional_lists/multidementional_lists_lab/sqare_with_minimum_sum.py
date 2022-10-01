rows, cols = [int(x) for x in input().split(", ")]

matrix = [list(map(int, input().split(', '))) for x in range(rows)]

sub_matrix = []

max_matrix = []
sub_matrix_value = 0

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        sub_matrix = []
        if j + 1 < len(matrix[i]):  # check this
            sub_matrix.append(matrix[i][j:j + 2])
        if i + 1 < len(matrix):
            if j + 1 < len(matrix[i]):
                sub_matrix.append(matrix[i + 1][j:j + 2])
        current_sum = 0
        for k in sub_matrix:
            current_sum += sum(k)

        if current_sum > sub_matrix_value:
            sub_matrix_value = current_sum
            max_matrix.clear()
            max_matrix = sub_matrix

for i in range(len(max_matrix)):
    for j in range(len(max_matrix[i])):
        if j != len(max_matrix[i]) - 1:
            print(max_matrix[i][j], end=" ")
        else:
            print(max_matrix[i][j])

print(sub_matrix_value)

lists_to_flatten = input().split("|")

matrix = []

for i in lists_to_flatten:
    matrix.append([i])

for i in range(len(matrix) - 1, -1, -1):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            if k < len(matrix[i][j]) - 1:
                if matrix[i][j][k] == " ":
                    continue
                elif matrix[i][j][k + 1] != " " and matrix[i][j][k] != " ":
                    print(matrix[i][j][k], end="")
                elif matrix[i][j][k] != " ":
                    print(matrix[i][j][k], end=" ")
            else:
                if matrix[i][j][k] != " ":
                    print(matrix[i][j][k], end=" ")

number_of_rows = int(input())

matrix = [list(map(int, input().split())) for i in range(number_of_rows)]

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            primary_diagonal.append(matrix[i][j])

for i in range(len(matrix)):
    for j in range(len(matrix[i]) - 1, -1, -1):
        if j == len(matrix[i]) - 1 - i:
            secondary_diagonal.append(matrix[i][j])

print(abs((sum(primary_diagonal)) - sum(secondary_diagonal)))

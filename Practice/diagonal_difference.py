n = int(input())

matrix = [list(map(int, input().split())) for r in range(n)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = []

for row in range(len(matrix) -1, -1, -1):
    for col in range(len(matrix[row])):
        if col == len(matrix) - 1 - row:
            secondary_diagonal.append(matrix[row][col])

difference = sum(primary_diagonal) - sum(secondary_diagonal)

print(abs(difference))




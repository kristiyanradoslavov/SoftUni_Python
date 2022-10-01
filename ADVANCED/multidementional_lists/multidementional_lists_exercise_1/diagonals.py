number_of_rows = int(input())

matrix = [list(map(int, input().split(", "))) for i in range(number_of_rows)]

primary_diagonal = [matrix[x][j] for x in range(len(matrix)) for j in range(len(matrix[x])) if x == j]
secondary_diagonal = [matrix[x][j] for x in range(len(matrix)) for j in range(len(matrix[x]) - 1, -1, -1) if
                      j == len(matrix[x]) - 1 - x]


print(f"Primary diagonal: ", end="")
for first in range(len(primary_diagonal)):
    if first == len(primary_diagonal) - 1:
        print(f"{primary_diagonal[first]}. Sum: {sum(primary_diagonal)}")
    else:
        print(primary_diagonal[first], end=", ")

print(f"Secondary diagonal: ", end="")
for second in range(len(secondary_diagonal)):
    if second == len(secondary_diagonal) - 1:
        print(f"{secondary_diagonal[second]}. Sum: {sum(secondary_diagonal)}")
    else:
        print(secondary_diagonal[second], end=", ")
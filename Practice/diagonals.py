rows = int(input())

matrix = [list(map(int, input().split(", "))) for r in range(rows)]

primary_diagonal = [matrix[c][r] for c in range(len(matrix)) for r in range(len(matrix[c])) if c == r]
secondary_diagonal = [matrix[c][r] for c in range(len(matrix) - 1, -1, -1) for r in range(len(matrix[c])) if
                      c == len(matrix) - 1 - r]

# for cols in range(len(matrix)):
#     primary_diagonal.append(matrix[cols][cols])
#
# for r in range(len(matrix) - 1, -1, -1):
#     for c in range(len(matrix[r]) - 1, -1, -1):
#         if c == len(matrix) - 1 - r:
#             secondary_diagonal.append(matrix[r][c])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal[::-1]))}. Sum: {sum(secondary_diagonal)}")

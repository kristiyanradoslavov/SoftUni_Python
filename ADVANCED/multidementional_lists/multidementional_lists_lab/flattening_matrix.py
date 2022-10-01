number_of_rows = int(input())

matrix = []

for _ in range(number_of_rows):
    matrix.append([int(x) for x in input().split(", ")])

final_matrix = [x for i in matrix for x in i]

print(final_matrix)

# !!!!!!@@@@@@@@This is normal for cycle with len!!!!!!!!!!@@@@@@
# final_matrix = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         final_matrix.append(matrix[i][j])
#
# print(final_matrix)

# !!!!!!!!!!!!This is normal for cycle with elements directly@@@@
# final_matrix = []
# for i in matrix:
#     for j in i:
#         final_matrix.append(j)
#
# print(final_matrix)
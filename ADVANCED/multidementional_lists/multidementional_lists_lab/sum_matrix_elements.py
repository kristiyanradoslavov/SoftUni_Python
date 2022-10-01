rows, cols = [int(x) for x in input().split(", ")]


matrix = []
total_sum = 0

for _ in range(cols):
    matrix.append([int(x) for x in input().split(", ")])

for col in range(cols):
    for row in range(rows):
        total_sum += matrix[col][row]

print(total_sum)
print(matrix)




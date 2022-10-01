rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(cols):
    current_sum = 0
    for j in range(rows):
        current_sum += matrix[j][i]
    print(current_sum)
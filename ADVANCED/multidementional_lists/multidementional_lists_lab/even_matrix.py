number_of_rows = int(input())


matrix = []

for i in range(number_of_rows):
    matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])

print(matrix)

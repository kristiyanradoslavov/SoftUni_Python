cols = int(input())

matrix = [list(map(int, input().split())) for x in range(cols)]

final_num = 0
for row in range(cols):
    final_num += matrix[row][row]

print(final_num)
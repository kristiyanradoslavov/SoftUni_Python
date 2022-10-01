def check_indices(current_row, current_col):
    result = False
    if -1 < current_row < len(matrix):
        if -1 < current_col < len(matrix[current_row]):
            result = True
    return result


rows = int(input())

matrix = [list(map(int, input().split())) for x in range(rows)]

current_input = input()

while current_input != "END":
    current_command = current_input.split()
    key_word = current_command[0]
    row = int(current_command[1])
    col = int(current_command[2])
    value = int(current_command[3])

    if key_word == "Add":
        if check_indices(row, col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif key_word == "Subtract":
        if check_indices(row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    # else:
    #     print()

    current_input = input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == len(matrix[i]) - 1:
            print(matrix[i][j])
        else:
            print(matrix[i][j], end=" ")
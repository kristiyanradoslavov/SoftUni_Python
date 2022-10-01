rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for x in range(rows)]

current_input = input()

while current_input != "END":
    current_command = current_input.split()
    command_is_valid = False
    if current_command[0] == "swap" and len(current_command) == 5:
        row_1_old = int(current_command[1])
        col_1_old = int(current_command[2])
        row_2_new = int(current_command[3])
        col_2_new = int(current_command[4])

        if (-1 < row_1_old < rows) and (-1 < row_2_new < rows):  # the input might not be digit have in mind
            if (-1 < col_1_old < cols) and (-1 < col_2_new < cols):
                command_is_valid = True
                first_value = matrix[row_1_old][col_1_old]
                second_value = matrix[row_2_new][col_2_new]
                matrix[row_1_old][col_1_old] = second_value
                matrix[row_2_new][col_2_new] = first_value
                for i in range(len(matrix)):
                    print(" ".join(matrix[i]))

    if not command_is_valid:
        print("Invalid input!")

    current_input = input()

# def check_current_knight(current_index, current_char, row):
#     if current_index + 2 < current_row_length:


size_of_the_board = int(input())

matrix = []

for i in range(size_of_the_board):
    matrix.append([])
    current_input = input()
    for j in range(len(current_input)):
        matrix[i].append(current_input[j])

matrix_length = len(matrix)


no_collisions_found = False
max_moves_on_the_board = 0
biggest_knight_row = 0
biggest_knight_col = 0

knights_removed = 0

while not no_collisions_found:
    for row in range(len(matrix)):
        for index, char in enumerate(matrix[row]):
            max_moves_on_knight = 0
            current_row_length = len(matrix[row])
            if char == "K":
                # from here cover horizontal movement downwards
                if index + 2 < current_row_length:
                    if row + 1 < matrix_length:
                        row_to_collide = row + 1
                        column_to_collide = index + 2
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                if index - 2 >= 0:
                    if row + 1 < matrix_length:
                        row_to_collide = row + 1
                        column_to_collide = index - 2
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1
                # from here cover horizontal movement upwards.

                if index + 2 < current_row_length:
                    if row - 1 >= 0:
                        row_to_collide = row - 1
                        column_to_collide = index + 2
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                if index - 2 >= 0:
                    if row - 1 >= 0:
                        row_to_collide = row - 1
                        column_to_collide = index - 2
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                # from here cover up vertical movements
                if row - 2 >= 0:
                    if index - 1 >= 0:
                        row_to_collide = row - 2
                        column_to_collide = index - 1
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                if row - 2 >= 0:
                    if index + 1 < current_row_length:
                        row_to_collide = row - 2
                        column_to_collide = index + 1
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                # from here cover down vertical movements

                if row + 2 < matrix_length:
                    if index - 1 >= 0:
                        row_to_collide = row + 2
                        column_to_collide = index - 1
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

                if row + 2 < matrix_length:
                    if index + 1 < current_row_length:
                        row_to_collide = row + 2
                        column_to_collide = index + 1
                        if matrix[row_to_collide][column_to_collide] == "K":
                            max_moves_on_knight += 1

            if max_moves_on_knight > max_moves_on_the_board:
                max_moves_on_the_board = max_moves_on_knight
                biggest_knight_row = row
                biggest_knight_col = index

    if max_moves_on_the_board == 0:
        break
    if max_moves_on_the_board > 0:
        matrix[biggest_knight_row][biggest_knight_col] = 0
        max_moves_on_the_board = 0
        knights_removed += 1

print(knights_removed)
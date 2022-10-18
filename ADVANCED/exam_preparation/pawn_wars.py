from collections import deque


def validation_check(row, col):
    result = False
    if 0 <= row < size and 0 <= col < size:
        result = True

    return result


def diagonal_check(pawn_color):
    result = False
    if pawn_color == "White":
        left_row, left_col = w_row - 1, w_col - 1
        right_row, right_col = w_row - 1, w_col + 1
        if validation_check(left_row, left_col):
            if matrix[left_row][left_col] == "b":
                result = True
                print(f"Game over! White win, capture on {letters[left_col]}{size - left_row}.")
        if validation_check(right_row, right_col):
            if matrix[right_row][right_col] == "b":
                result = True
                print(f"Game over! White win, capture on {letters[right_col]}{size - right_row}.")

    elif pawn_color == "Black":
        left_row, left_col = b_row + 1, b_col - 1
        right_row, right_col = b_row + 1, b_col + 1
        if validation_check(left_row, left_col):
            if matrix[left_row][left_col] == "w":
                result = True
                print(f"Game over! Black win, capture on {letters[left_col]}{size - left_row}.")
        if validation_check(right_row, right_col):
            if matrix[right_row][right_col] == "w":
                result = True
                print(f"Game over! Black win, capture on {letters[right_col]}{size - right_row}.")

    return result


size = 8
matrix = []
w_row, w_col = 0, 0
b_row, b_col = 0, 0

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(size):
    current_row = input().split()
    if "w" in current_row:
        w_row, w_col = i, current_row.index("w")

    if "b" in current_row:
        b_row, b_col = i, current_row.index("b")

    matrix.append(current_row)

pawns = deque(["White", "Black"])

while True:
    current_pawn = pawns.popleft()
    pawns.append(current_pawn)
    if diagonal_check(current_pawn):
        break
    else:
        if current_pawn == "White":
            matrix[w_row][w_col] = "-"
            w_row -= 1
            matrix[w_row][w_col] = "w"
            if w_row == 0:
                print(f"Game over! White pawn is promoted to a queen at {letters[w_col]}{size - w_row}.")
                break
        elif current_pawn == "Black":
            matrix[b_row][b_col] = "-"
            b_row += 1
            matrix[b_row][b_col] = "b"
            if b_row == size - 1:
                print(f"Game over! Black pawn is promoted to a queen at {letters[b_col]}{size - b_row}.")
                break

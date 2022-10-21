def sum_row(m_col):
    points = 0
    for current_num in matrix:
        if current_num[m_col].isdigit():
            points += int(current_num[m_col])

    return points


size = 6
matrix = [input().split() for x in range(size)]

total_points = 0

for trow in range(3):
    row_pos, col_pos = list(map(int, input().strip("()").split(", ")))

    if 0 <= row_pos < size and 0 <= col_pos < size:
        if matrix[row_pos][col_pos] == "B":
            total_points += sum_row(col_pos)
            matrix[row_pos][col_pos] = "X"

if 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")

elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")

elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")

else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
from collections import deque

size = 7
players = deque(input().split(", "))
players_points = {
    players[0]: [501, 0],
    players[1]: [501, 0]
}

matrix = [input().split() for x in range(size)]
winner = ""
hit_bullseye = False

while players_points[players[0]][0] > 0 and players_points[players[1]][0] > 0:

    throw_row, throw_col = map(int, input().strip("()").split(", "))
    current_player = players.popleft()
    players.append(current_player)

    if 0 <= throw_row < size and 0 <= throw_col < size:
        if matrix[throw_row][throw_col].isdigit():
            num = matrix[throw_row][throw_col]
            players_points[current_player][0] -= int(num)
            players_points[current_player][1] += 1

        elif matrix[throw_row][throw_col] == "D":
            row_nums = int(matrix[throw_row][0]) + int(matrix[throw_row][-1])
            col_nums = int(matrix[0][throw_col]) + int(matrix[-1][throw_col])
            final_num = (row_nums + col_nums) * 2
            players_points[current_player][0] -= int(final_num)
            players_points[current_player][1] += 1

        elif matrix[throw_row][throw_col] == "T":
            row_nums = int(matrix[throw_row][0]) + int(matrix[throw_row][-1])
            col_nums = int(matrix[0][throw_col]) + int(matrix[-1][throw_col])
            final_num = (row_nums + col_nums) * 3
            players_points[current_player][0] -= int(final_num)
            players_points[current_player][1] += 1

        elif matrix[throw_row][throw_col] == "B":
            players_points[current_player][1] += 1
            winner = current_player
            hit_bullseye = True
            break
    else:
        players_points[current_player][1] += 1

if not hit_bullseye:
    for key, value in players_points.items():
        if value[0] <= 0:
            print(f"{key} won the game with {value[1]} throws!")
            break

else:
    print(f"{winner} won the game with {players_points[winner][1]} throws!")

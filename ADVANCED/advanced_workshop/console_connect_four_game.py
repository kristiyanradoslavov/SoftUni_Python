from collections import deque


def print_matrix(current_matrix):
    for i in range(matrix_rows):
        print(matrix[i])


def check_for_win(current_matrix, player):
    player_wins = False

    for current_row in range(matrix_rows):
        for current_col in range(matrix_cols):
            for i in range(len(directions)):
                r, c = (
                    current_row + directions[i][0],
                    current_col + directions[i][1]
                )
                for iterations in range(4):
                    if 0 <= r < matrix_rows and 0 <= c < matrix_cols:
                        if current_matrix[r][c] != player:
                            break
                    else:
                        break
                    r += directions[i][0]
                    c += directions[i][1]

                else:
                    player_wins = True

    return player_wins


matrix_rows, matrix_cols = 6, 7
matrix = []
game_is_won = False

for rows in range(matrix_rows):
    matrix.append([])
    for cols in range(matrix_cols):
        matrix[rows].append(0)

symbols = {
    "Player 1": 1,
    "Player 2": 2
}

directions = (
    (-1, 0,),
    (1, 0,),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
)

players_turns = deque(["Player 1", "Player 2"])
print()
print("CONSOLE CONNECT FOUR")
print()
print("Rules: This is a two players game, each player chooses a column in the range 1 - 7 to place his symbol.")
print("The first player who manages to connect 4 symbols in a row - horizontally, vertically or diagonally, wins \
the game!")
print()

while True:
    try:
        player_command = int(input(f"{players_turns[0]} please choose a column: "))
    except ValueError:
        print(f"Invalid column, please choose column in the range 1 - {matrix_cols}")
        continue

    if player_command > matrix_cols or player_command <= 0:
        print(f"Invalid column, please choose column in the range 1 - {matrix_cols}")
        continue

    if matrix[0][player_command - 1] != 0:
        print("This row is already full, please choose a different one!")
        continue

    current_player = players_turns.popleft()
    players_turns.append(current_player)

    for i in range(matrix_rows):
        row, col = i, player_command - 1
        if matrix[row][col] != 0:
            matrix[row - 1][col] = symbols[current_player]
            if check_for_win(matrix, symbols[current_player]):
                game_is_won = True
            break
        elif i == matrix_rows - 1:
            matrix[row][col] = symbols[current_player]
            if check_for_win(matrix, symbols[current_player]):
                game_is_won = True

    print_matrix(matrix)

    if game_is_won:
        print(f"Player {symbols[current_player]} wins the game.")
        break

from collections import deque


def print_the_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == len(board[row]) - 1:
                print(f"| {board[row][col]} |")
            else:
                print(f"| {board[row][col]} ", end="")


def check_position(board, position):
    result = False

    real_position = position - 1
    if 0 <= real_position < 3:
        if board[0][real_position] == "X" or board[0][real_position] == "O":
            print("Position already taken !")
            result = True
    elif 3 <= real_position < 6:
        if board[1][real_position - 3] == "X" or board[1][real_position - 3] == "O":
            print("Position already taken !")
            result = True
    elif 6 <= real_position < 9:
        if board[2][real_position - 6] == "X" or board[2][real_position - 6] == "O":
            print("Position already taken !")
            result = True

        print("Position already taken !")

    return result


def append_num(position):
    real_position = position - 1
    if 0 <= real_position < 3:
        board_numeration_matrix[0][real_position] = (player_symbol_information[current_player])
    elif 3 <= real_position < 6:
        board_numeration_matrix[1][real_position - 3] = (player_symbol_information[current_player])
    elif 6 <= real_position < 9:
        board_numeration_matrix[2][real_position - 6] = (player_symbol_information[current_player])


player_one = input("Player one name: ")
player_two = input("Player two name: ")
available_symbols = ["X", "O"]
player_one_symbol = ""
player_two_symbol = ""

while True:
    player_one_symbol = input(f"{player_one} would you like to play with 'X' or 'O' ?  ").upper()
    if player_one_symbol.upper() != "X" and player_one_symbol.upper() != "O":
        print("Wrong input !")
        continue
    available_symbols.remove(player_one_symbol)
    player_two_symbol = available_symbols[0]
    break

board_numeration_matrix = []
board_empty_matrix = []

num = 1

for row in range(3):
    board_empty_matrix.append([])
    board_numeration_matrix.append([])
    for col in range(3):
        board_empty_matrix[row].append(num)
        board_numeration_matrix[row].append("")
        num += 1

print("This is the numeration of the board:")
print_the_board(board_empty_matrix)
print()
print(f"{player_one} starts first!")

player_symbol_information = {
    player_one: player_one_symbol,
    player_two: player_two_symbol
}

players = deque([player_one, player_two])

while True:
    try:
        current_symbol = int(input(f"{players[0]} choose a free position [1-9]: "))
        if current_symbol < 1 or current_symbol > 9:
            print("Invalid position!")
            continue
        if check_position(board_numeration_matrix, current_symbol):
            continue
        else:
            current_player = players.popleft()
            players.append(current_player)
            append_num(current_symbol)

    except ValueError:
        print("Invalid command!")
        continue

    print_the_board(board_numeration_matrix)

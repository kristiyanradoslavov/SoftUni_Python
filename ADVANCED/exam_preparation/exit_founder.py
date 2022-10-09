from collections import deque

players = deque(input().split(", "))

matrix = [input().split() for x in range(6)]

dict_players = {
    players[0]: False,
    players[1]: False,
}

while True:
    coordinates = list(map(int, input().strip("(").strip(")").split(", ")))
    row, col = coordinates[0], coordinates[1]

    current_player = players.popleft()
    players.append(current_player)
    if dict_players[current_player] is True:
        dict_players[current_player] = False
        continue

    if 0 <= row < 6 and 0 <= col < 6:
        if matrix[row][col] == "E":
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{current_player} is out of the game! The winner is {players.popleft()}.")
            break
        elif matrix[row][col] == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            dict_players[current_player] = True

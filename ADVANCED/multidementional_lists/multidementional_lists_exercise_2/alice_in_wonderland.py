size = int(input())

matrix = []
alice_position = []
tea_bags = 0

for row in range(size):
    current_row = input().split()
    if "A" in current_row:
        alice_position = [row, current_row.index("A")]
    matrix.append(current_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while tea_bags < 10:
    command = input()
    matrix[alice_position[0]][alice_position[1]] = "*"

    row, col = [
        alice_position[0] + directions[command][0],
        alice_position[1] + directions[command][1]
    ]

    if 0 <= row < size and 0 <= col < size:
        alice_position = [row, col]

        if matrix[row][col].isdigit():
            tea_bags += int(matrix[row][col])
            matrix[row][col] = "*"
        elif matrix[row][col] == "R":
            matrix[row][col] = "*"
            break

    else:
        break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in range(size):
    print(*matrix[row])
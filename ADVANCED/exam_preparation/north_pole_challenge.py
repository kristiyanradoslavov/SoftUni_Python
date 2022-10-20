def check_for_decor(row, col, matrix, decors, gif, cook, starting_d, starting_g, starting_c):
    if matrix[row][col] == "D":
        decors += 1
        starting_d -= 1
    elif matrix[row][col] == "G":
        gif += 1
        starting_g -= 1
    elif matrix[row][col] == "C":
        cook += 1
        starting_c -= 1

    return decors, gif, cook, starting_d, starting_g, starting_c


m_row, m_col = map(int, input().split(", "))

my_pos = []
matrix = []

starting_decorations = 0
starting_gifts = 0
starting_cookies = 0

for i in range(m_row):
    current_row = input().split()
    if "Y" in current_row:
        my_pos.extend((i, current_row.index("Y")))
    for j in current_row:
        if "D" == j:
            starting_decorations += 1
        elif "C" == j:
            starting_cookies += 1
        elif "G" == j:
            starting_gifts += 1

    matrix.append(current_row)

directions_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

christmas_decorations = 0
gifts = 0
cookies = 0
all_items_collected = False

command = input()

while command != "End":
    direction, steps = command.split("-")

    for i in range(int(steps)):
        row, col = (
            my_pos[0],
            my_pos[1]
        )

        n_row = directions_dict[direction][0] + row
        n_col = directions_dict[direction][1] + col
        if 0 <= n_row < m_row and 0 <= n_col < m_col:
            matrix[row][col] = "x"
            christmas_decorations, gifts, cookies, starting_decorations, starting_gifts, starting_cookies = \
                check_for_decor(n_row, n_col, matrix, christmas_decorations, gifts, cookies,
                                starting_decorations, starting_gifts, starting_cookies)

            matrix[n_row][n_col] = "Y"
            my_pos[0] = n_row
            my_pos[1] = n_col

        else:
            if direction == "left":
                matrix[row][col] = "x"
                my_pos[1] = m_col - 1
                christmas_decorations, gifts, cookies, starting_decorations, starting_gifts, starting_cookies = \
                    check_for_decor(n_row, my_pos[1], matrix, christmas_decorations, gifts, cookies,
                                    starting_decorations, starting_gifts, starting_cookies)

            elif direction == "right":
                matrix[row][col] = "x"
                my_pos[1] = 0
                christmas_decorations, gifts, cookies, starting_decorations, starting_gifts, starting_cookies = \
                    check_for_decor(n_row, my_pos[1], matrix, christmas_decorations, gifts, cookies,
                                    starting_decorations, starting_gifts, starting_cookies)

            elif direction == "up":
                matrix[row][col] = "x"
                my_pos[0] = m_row - 1
                christmas_decorations, gifts, cookies, starting_decorations, starting_gifts, starting_cookies = \
                    check_for_decor(my_pos[0], n_col, matrix, christmas_decorations, gifts, cookies,
                                    starting_decorations, starting_gifts, starting_cookies)

            elif direction == "down":
                matrix[row][col] = "x"
                my_pos[0] = 0
                christmas_decorations, gifts, cookies, starting_decorations, starting_gifts, starting_cookies = \
                    check_for_decor(my_pos[0], n_col, matrix, christmas_decorations, gifts, cookies,
                                    starting_decorations, starting_gifts, starting_cookies)

            matrix[my_pos[0]][my_pos[1]] = "Y"

        if starting_gifts == 0 and starting_decorations == 0 and starting_cookies == 0:
            all_items_collected = True
            break

    if all_items_collected:
        break
    command = input()

if all_items_collected:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {christmas_decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for i in matrix:
    print(*i)

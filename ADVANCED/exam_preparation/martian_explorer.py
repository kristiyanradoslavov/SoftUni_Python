size = 6

matrix = []
rover_row, rover_col = (0, 0)

for i in range(size):
    input_row = input().split()
    if "E" in input_row:
        rover_row, rover_col = (i, input_row.index("E"))
    matrix.append(input_row)

input_commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
water = 0
concrete = 0
metal = 0
area_is_suitable = False

for current_command in input_commands:
    rover_row += directions[current_command][0]
    rover_col += directions[current_command][1]

    if (rover_col < 0 or rover_col >= size) or (rover_row < 0 or rover_row >= size):
        if current_command == "up":
            rover_row = size - 1
        elif current_command == "down":
            rover_row = 0
        elif current_command == "left":
            rover_col = size - 1
        elif current_command == "right":
            rover_col = 0

    if matrix[rover_row][rover_col] == "W":
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

    if water >= 1 and concrete >= 1 and metal >= 1:
        area_is_suitable = True

if area_is_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

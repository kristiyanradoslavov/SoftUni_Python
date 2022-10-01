fire_level = input()
amount_of_water = int(input())

list_of_fires = fire_level.split("#")
list_of_cells = []
total_effort = 0
amount_is_valid = False

while amount_of_water > 0:
    for fires in range(0, len(list_of_fires)):
        current_fire = list_of_fires[fires].split(' ')
        if 81 <= int(current_fire[2]) <= 125 and str(current_fire[0]) == "High":
            amount_is_valid = True
        elif 51 <= int(current_fire[2]) <= 80 and str(current_fire[0]) == "Medium":
            amount_is_valid = True
        elif 1 <= int(current_fire[2]) <= 50 and str(current_fire[0]) == "Low":
            amount_is_valid = True

        if amount_is_valid:
            effort = 0.25 * int(current_fire[2])
            if amount_of_water < int(current_fire[2]):
                continue
            amount_of_water -= int(current_fire[2])
            list_of_cells.append(int(current_fire[2]))
            total_effort += effort
            amount_is_valid = False
    if amount_of_water > 0:
        break


total_fire = sum(list_of_cells)
print("Cells:")
for i in list_of_cells:
    print(f"- {int(i)}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")




def check_stone_availability(stone_name,stone_count):
    if stone_name not in material_dict:
        material_dict[stone_name] = int(stone_count)
    else:
        material_dict[stone_name] += int(stone_count)


command = input()

goal_reached = False
material_dict = {}
shadowmourne = False
valanyr = False
dragonwrath = False

while not goal_reached:
    current_command = command.split(" ")
    stone_index = 1
    count_index = 0
    length_half = len(current_command) / 2

    for stone in range(0, int(length_half)):
        stones = current_command[stone_index].lower()
        counts = current_command[count_index]
        if stones == "shards":
            check_stone_availability(stones, counts)
            if material_dict["shards"] >= 250:
                goal_reached = True
                shadowmourne = True
                material_dict["shards"] -= 250
                break
        elif stones == "fragments":
            check_stone_availability(stones, counts)
            if material_dict["fragments"] >= 250:
                goal_reached = True
                valanyr = True
                material_dict["fragments"] -= 250
                break
        elif stones == "motes":
            check_stone_availability(stones, counts)
            if material_dict["motes"] >= 250:
                goal_reached = True
                dragonwrath = True
                material_dict["motes"] -= 250
                break
        else:
            check_stone_availability(stones, counts)

        stone_index += 2
        count_index += 2

    if goal_reached:
        break

    command = input()

if valanyr:
    print("Valanyr obtained!")
elif shadowmourne:
    print("Shadowmourne obtained!")
elif dragonwrath:
    print("Dragonwrath obtained!")

if "shards" in material_dict:
    print(f'shards: {material_dict.pop("shards")}')
else:
    print("shards: 0")

if "fragments" in material_dict:
    print(f'fragments: {material_dict.pop("fragments")}')
else:
    print("fragments: 0")

if "motes" in material_dict:
    print(f'motes: {material_dict.pop("motes")}')
else:
    print("motes: 0")

for key, value in material_dict.items():
    print(f"{key}: {value}")
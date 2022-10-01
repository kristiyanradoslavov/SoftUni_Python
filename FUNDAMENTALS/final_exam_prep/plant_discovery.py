def plant_validation(plant_name):
    func_result = False
    if plant_name not in all_plants_dictionary:
        print("error")
        func_result = True
    return func_result


count_of_plants = int(input())

all_plants_dictionary = {}
for all_plants in range(count_of_plants):
    current_plant = input().split("<->")
    key = current_plant[0]
    value = int(current_plant[1])
    if key in all_plants_dictionary:
        all_plants_dictionary[key]["Rarity"] = value
    else:
        all_plants_dictionary[key] = {}
        all_plants_dictionary[key]["Rarity"] = value
        all_plants_dictionary[key]["Rating"] = []

command = input()

while command != "Exhibition":
    current_command = command.split(": ")
    essential_command = current_command[0]
    if essential_command == "Rate":
        remaining_information = current_command[1].split(" - ")
        plant_to_rate = remaining_information[0]
        rating = int(remaining_information[1])
        if plant_validation(plant_to_rate):
            command = input()
            continue
        all_plants_dictionary[plant_to_rate]["Rating"].append(rating)
    elif essential_command == "Update":
        remaining_information_2 = current_command[1].split(" - ")
        plant_to_change_rarity = remaining_information_2[0]
        new_rarity = int(remaining_information_2[1])
        if plant_validation(plant_to_change_rarity):
            command = input()
            continue
        all_plants_dictionary[plant_to_change_rarity]["Rarity"] = new_rarity
    elif essential_command == "Reset":
        plant = current_command[1]
        if plant_validation(plant):
            command = input()
            continue
        all_plants_dictionary[plant]["Rating"].clear()

    command = input()

print("Plants for the exhibition:")
for curr_key, curr_value in (all_plants_dictionary.items()):
    length = len(all_plants_dictionary[curr_key]["Rating"])
    total_amount = sum(all_plants_dictionary[curr_key]["Rating"])
    result = 0
    if total_amount != 0:
        result = total_amount/length
    print(f"- {curr_key}; Rarity: {curr_value['Rarity']}; Rating: {result:.2f}")
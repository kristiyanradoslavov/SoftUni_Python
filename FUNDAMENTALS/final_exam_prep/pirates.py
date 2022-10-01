# Function which creates new cities in the dict or adds population and gold to existing ones.
def new_cities(current_city, current_pop, current_gold):
    if current_city in city_collection_dict:
        city_collection_dict[current_city]["Population"] += current_pop
        city_collection_dict[current_city]["Gold"] += current_gold
    else:
        city_collection_dict[current_city] = {}
        city_collection_dict[current_city]["Population"] = current_pop
        city_collection_dict[current_city]["Gold"] = current_gold


def plundered_city(current_town, current_people, current_gold):
    if city_collection_dict[current_town]["Population"] > 0 and city_collection_dict[current_town]["Gold"] > 0:
        city_collection_dict[current_town]["Population"] -= current_people
        city_collection_dict[current_town]["Gold"] -= current_gold
        print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")
        if city_collection_dict[current_town]["Population"] <= 0 or city_collection_dict[current_town]["Gold"] <= 0:
            del city_collection_dict[current_town]
            print(f"{current_town} has been wiped off the map!")


def prosper_city(current_town, current_gold):
    if current_gold <= 0:
        print("Gold added cannot be a negative number!")
    else:
        city_collection_dict[current_town]["Gold"] += current_gold
        print(f"{current_gold} gold added to the city treasury. \
{current_town} now has {city_collection_dict[current_town]['Gold']} gold.")


first_command = input()

city_collection_dict = {}

while first_command != "Sail":
    current_first_command = first_command.split("||")
    city = current_first_command[0]
    population = int(current_first_command[1])
    gold = int(current_first_command[2])
    new_cities(city, population, gold)

    first_command = input()

second_command = input()
while second_command != "End":
    current_second_command = second_command.split("=>")
    key_command = current_second_command[0]
    if key_command == "Plunder":
        town_to_plunder = current_second_command[1]
        people_to_kill = int(current_second_command[2])
        gold_to_plunder = int(current_second_command[3])
        plundered_city(town_to_plunder, people_to_kill, gold_to_plunder)
    elif key_command == "Prosper":
        town_to_prosper = current_second_command[1]
        gold_to_add = int(current_second_command[2])
        prosper_city(town_to_prosper, gold_to_add)

    second_command = input()

if city_collection_dict:
    print(f"Ahoy, Captain! There are {len(city_collection_dict)} wealthy settlements to go to:")
    for key, value in city_collection_dict.items():
        print(f"{key} -> Population: {value['Population']} citizens, Gold: {value['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


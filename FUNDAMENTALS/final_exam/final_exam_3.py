def good_meals(guest, meal):
    if guest not in meal_and_guest_information:
        meal_and_guest_information[guest] = []
        meal_and_guest_information[guest].append(meal)
    elif (guest in meal_and_guest_information) and (meal not in meal_and_guest_information[guest]):
        meal_and_guest_information[guest].append(meal)


def bad_meals(guest, meal):
    if guest not in meal_and_guest_information:
        print(f"{guest} is not at the party.")
    else:
        if meal in meal_and_guest_information[guest]:
            meal_and_guest_information[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            if meal not in unliked_meals:
                unliked_meals.append(meal)
        else:
            print(f"{guest} doesn't have the {meal} in his/her collection.")


meal_and_guest_information = {}
unliked_meals = []
command = input()

while command != "Stop":
    current_command = command.split("-")
    key_command = current_command[0]
    if key_command == "Like":
        guest_likes = current_command[1]
        liked_meal = current_command[2]
        good_meals(guest_likes, liked_meal)
    elif key_command == "Dislike":
        guest_dislikes = current_command[1]
        disliked_meal = current_command[2]
        bad_meals(guest_dislikes, disliked_meal)

    command = input()

for key, value in meal_and_guest_information.items():
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {len(unliked_meals)}")
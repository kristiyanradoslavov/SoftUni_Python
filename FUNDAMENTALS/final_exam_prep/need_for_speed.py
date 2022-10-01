def add_new_car(car, mileage, fuel):
    all_cars_dict[car] = {}
    all_cars_dict[car]["mileage"] = mileage
    all_cars_dict[car]["fuel"] = fuel


def drive_the_car(car, distance, fuel):
    if all_cars_dict[car]["fuel"] >= fuel:
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        all_cars_dict[car]["mileage"] += distance
        all_cars_dict[car]["fuel"] -= fuel
    else:
        print("Not enough fuel to make that ride")
    if all_cars_dict[car]["mileage"] >= 100000:
        del all_cars_dict[car]
        print(f"Time to sell the {car}!")


def refuel_car(car, fuel):
    result = all_cars_dict[car]["fuel"] + fuel
    if result > 75:
        difference = 75 - all_cars_dict[car]["fuel"]
        all_cars_dict[car]["fuel"] = 75
        print(f"{car} refueled with {difference} liters")
    else:
        all_cars_dict[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert_mileage(car, kilometers):
    result = all_cars_dict[car]["mileage"] - kilometers
    if result < 10000:
        all_cars_dict[car]["mileage"] = 10000
    else:
        all_cars_dict[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")


number_of_cars = int(input())

all_cars_dict = {}
for _ in range(number_of_cars):
    current_car = input().split("|")
    new_car = current_car[0]
    new_car_mileage = int(current_car[1])
    new_car_fuel = int(current_car[2])
    add_new_car(new_car, new_car_mileage, new_car_fuel)


command = input()
while command != "Stop":
    current_command = command.split(" : ")
    key_command = current_command[0]
    if key_command == "Drive":
        car_to_drive = current_command[1]
        distance_to_drive = int(current_command[2])
        fuel_to_drive = int(current_command[3])
        drive_the_car(car_to_drive, distance_to_drive, fuel_to_drive)
    elif key_command == "Refuel":
        car_to_refuel = current_command[1]
        fuel_to_refuel = int(current_command[2])
        refuel_car(car_to_refuel, fuel_to_refuel)
    elif key_command == "Revert":
        car_to_decrease = current_command[1]
        kilometers_to_decrease = int(current_command[2])
        revert_mileage(car_to_decrease, kilometers_to_decrease)
    command = input()

for key, value in all_cars_dict.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

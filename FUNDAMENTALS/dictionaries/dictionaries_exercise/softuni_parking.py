count_of_registrations = int(input())

all_cars = {}


for registrations in range(count_of_registrations):
    current_command = input().split(" ")
    username = current_command[1]
    if current_command[0] == "register":
        license_plate = current_command[2]
        if username in all_cars:
            print(f"ERROR: already registered with plate number {all_cars[username]}")
        else:
            all_cars[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif current_command[0] == "unregister":
        if username not in all_cars:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del all_cars[username]

for key, item in all_cars.items():
    print(f"{key} => {item}")

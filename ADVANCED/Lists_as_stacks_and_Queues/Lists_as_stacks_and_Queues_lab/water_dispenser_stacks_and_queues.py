from collections import deque

people_who_want_water = deque()

quantity_of_water = int(input())

while True:
    people = input()
    if people == "Start":
        break
    people_who_want_water.append(people)

command = input()
while command != "End":
    current_command = command.split(" ")
    if len(current_command) > 1:
        liters_ref = int(current_command[1])
        quantity_of_water += liters_ref
    else:
        current_person = people_who_want_water.popleft()
        current_liters = current_command[0]
        liters = int(current_liters)
        if quantity_of_water >= liters:
            print(f"{current_person} got water")
            quantity_of_water -= liters
        else:
            print(f"{current_person} must wait")

    command = input()

print(f"{quantity_of_water} liters left")
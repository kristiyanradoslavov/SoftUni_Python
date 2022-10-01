from collections import deque

count_of_pump_locations = int(input())

amount_of_petrol = deque()
kilometers = deque()

for _ in range(count_of_pump_locations):
    current_input = input().split()
    current_petrol = int(current_input[0])
    distance = int(current_input[1])
    amount_of_petrol.append(current_petrol)
    kilometers.append(distance)

position = 0
position_found = False
total_fuel_in_truck = 0

while position_found is False:
    for current_index in range(len(amount_of_petrol)):
        current_fuel = amount_of_petrol[current_index]
        total_fuel_in_truck += current_fuel
        kilometers_to_go = kilometers[current_index]
        if total_fuel_in_truck >= kilometers_to_go:
            total_fuel_in_truck -= kilometers_to_go
            if current_index == len(amount_of_petrol) - 1:
                position_found = True
        else:
            amount_of_petrol.append(amount_of_petrol.popleft())
            kilometers.append(kilometers.popleft())
            position += 1
            total_fuel_in_truck = 0
            break

print(position)
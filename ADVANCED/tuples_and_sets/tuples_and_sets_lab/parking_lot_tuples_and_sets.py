count_of_cars = int(input())

car_set = set()

for _ in range(count_of_cars):
    direction, current_car = input().split(", ")
    if direction == "IN":
        car_set.add(current_car)
    elif direction == "OUT":
        if current_car in car_set:
            car_set.remove(current_car)

if car_set:
    for car in car_set:
        print(car)
else:
    print("Parking Lot is Empty")
clothes = list(map(int, input().split(" ")))
rack_capacity = int(input())

clothes_on_the_rack = 0
rack_counter = 1

while clothes:
    if clothes[-1] + clothes_on_the_rack <= rack_capacity:
        current_clothes = clothes.pop()
        clothes_on_the_rack += current_clothes
    else:
        rack_counter += 1
        clothes_on_the_rack = 0

print(rack_counter)
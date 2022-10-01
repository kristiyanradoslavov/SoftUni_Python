from collections import deque


def check_presents(level):
    doll = 150
    train = 250
    bear = 300
    bicycle = 400

    if level == doll:
        if "Doll" not in crafted_toys:
            crafted_toys["Doll"] = 0
        crafted_toys["Doll"] += 1
        remove_materials()
    elif level == train:
        if "Wooden train" not in crafted_toys:
            crafted_toys["Wooden train"] = 0
        crafted_toys["Wooden train"] += 1
        remove_materials()
    elif level == bear:
        if "Teddy bear" not in crafted_toys:
            crafted_toys["Teddy bear"] = 0
        crafted_toys["Teddy bear"] += 1
        remove_materials()
    elif level == bicycle:
        if "Bicycle" not in crafted_toys:
            crafted_toys["Bicycle"] = 0
        crafted_toys["Bicycle"] += 1
        remove_materials()
    else:
        found_difference()


def found_difference():
    magic_level.popleft()
    number_of_materials[-1] += 15


def remove_materials():
    number_of_materials.pop()
    magic_level.popleft()


number_of_materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

crafted_toys = {}
while number_of_materials:
    if not magic_level:
        break

    current_magic_level = number_of_materials[-1] * magic_level[0]
    if current_magic_level < 0:
        neg_result = number_of_materials[-1] + magic_level[0]
        remove_materials()
        number_of_materials.append(neg_result)
    elif (number_of_materials[-1] == 0) and (magic_level[0] == 0):
        remove_materials()
    elif number_of_materials[-1] == 0:
        number_of_materials.pop()
    elif magic_level[0] == 0:
        magic_level.popleft()

    else:
        check_presents(current_magic_level)

if ("Doll" in crafted_toys.keys() and "Wooden train" in crafted_toys.keys()) \
        or ("Teddy bear" in crafted_toys.keys() and "Bicycle" in crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if number_of_materials:
    print("Materials left: ", end="")
    for i in range(len(number_of_materials) -1, -1, -1):
        if i == 0:
            print(number_of_materials[i])
        else:
            print(number_of_materials[i], end=", ")

elif magic_level:
    print("Magic left: ", end="")
    for i in range(len(magic_level)):
        if i == len(magic_level) - 1:
            print(magic_level[i])
        else:
            print(magic_level[i], end=", ")

if crafted_toys:
    for key, value in sorted(crafted_toys.items()):
        print(f"{key}: {value}")

from collections import deque


def check_result(sum):
    if 100 <= sum <= 199:
        materials_dict["Gemstone"] += 1
    elif 200 <= sum <= 299:
        materials_dict["Porcelain Sculpture"] += 1
    elif 300 <= sum <= 399:
        materials_dict["Gold"] += 1
    elif 400 <= sum <= 499:
        materials_dict["Diamond Jewellery"] += 1


materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

materials_dict = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic:
    current_mat = materials.pop()
    current_magic = magic.popleft()
    result_to_compare = current_mat + current_magic

    if result_to_compare < 100:
        if result_to_compare % 2 == 0:
            current_mat *= 2
            current_magic *= 3
            result_to_compare = current_mat + current_magic
        else:
            current_mat *= 2
            current_magic *= 2
            result_to_compare = current_mat + current_magic

        check_result(result_to_compare)

    elif result_to_compare > 499:
        new_sum = result_to_compare / 2

        check_result(new_sum)

    else:
        check_result(result_to_compare)

if (materials_dict["Gemstone"] > 0 and materials_dict["Porcelain Sculpture"] > 0) \
        or \
        (materials_dict["Gold"] > 0 and materials_dict["Diamond Jewellery"] > 0):

    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for key, value in sorted(materials_dict.items()):
    if value > 0:
        print(f"{key}: {value}")
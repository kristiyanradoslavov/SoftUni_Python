def start_spring(**kwargs):
    type_dict = {}
    for key, value in kwargs.items():
        if value not in type_dict:
            type_dict[value] = []
        type_dict[value].append(key)

    for key in type_dict.keys():
        type_dict[key] = sorted(type_dict[key])

    sorted_dict = sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    final_string = ""

    for i in range(len(sorted_dict)):
        for j in range(len(sorted_dict[i])):
            final_string += f"{sorted_dict[i][0]}:\n"
            for k in sorted_dict[i][1]:
                final_string += f"-{k}\n"
            break

    return final_string[:-1]


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))




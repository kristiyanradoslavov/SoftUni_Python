def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key= lambda x: (-len(x[1]), (x[0])))

    final_list = []

    for key, value in result:
        final_list.append(key)
        sorted_list = sorted(value, reverse=True)
        final_list += sorted_list
    return "\n".join(str(x) for x in final_list)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

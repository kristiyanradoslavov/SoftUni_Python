def grocery_store(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: ((-x[1]), (-len(x[0])), (x[0])))
    result = ""

    for i in range(len(sorted_dict)):
        for j in range(len(sorted_dict[i])):
            if j == len(sorted_dict[i]) - 1:
                result += str(sorted_dict[i][j])
                result += "\n"
            else:
                result += str(sorted_dict[i][j]) + ": "

    return result[:-1]


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

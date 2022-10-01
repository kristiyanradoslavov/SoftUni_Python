def age_assignment(*args, **kwargs):
    new_dict = {}
    for i in kwargs.keys():
        for j in args:
            if i == j[0]:
                new_dict[j] = kwargs[i]
    result = ""
    sorted_result = sorted(new_dict.items())

    for i in range(len(sorted_result)):
        for j in range(len(sorted_result[i])):
            if j == len(sorted_result[i]) - 1:
                result += f"{sorted_result[i][j]} years old.\n"
            else:
                result += f'{sorted_result[i][j]} is '

    return result[:-1]


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

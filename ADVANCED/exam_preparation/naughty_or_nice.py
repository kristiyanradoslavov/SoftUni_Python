def naughty_or_nice_list(*args, **kwargs):
    nice_kids = []
    naughty_kids = []
    not_found = []

    santa_list = args[0]

    if len(args) > 1:
        arguments = args[1:]
        for current_command in arguments:
            number, command = current_command.split("-")
            if command == "Naughty":
                func_result = check_num(santa_list, number)
                if func_result is not None:
                    bad_kid = func_result[1]
                    naughty_kids.append(bad_kid[1])
                    santa_list.remove(bad_kid)

            elif command == "Nice":
                func_result = check_num(santa_list, number)
                if func_result is not None:
                    good_kid = func_result[1]
                    nice_kids.append(good_kid[1])
                    santa_list.remove(good_kid)

    if kwargs:
        for key, value in kwargs.items():
            if value == "Naughty":
                f_result = check_names(santa_list, key)
                if f_result is not None:
                    b_kid = f_result[1]
                    naughty_kids.append(b_kid[1])
                    santa_list.remove(b_kid)
            elif value == "Nice":
                f_result = check_names(santa_list, key)
                if f_result is not None:
                    g_kid = f_result[1]
                    nice_kids.append(g_kid[1])
                    santa_list.remove(g_kid)

    for kid in santa_list:
        not_found.append(kid[1])

    final_result = ""
    if nice_kids:
        final_result += "Nice: "
        for i in range(len(nice_kids)):
            if i == len(nice_kids) - 1:
                final_result += f"{nice_kids[i]}\n"
            else:
                final_result += f"{nice_kids[i]}, "

    if naughty_kids:
        final_result += "Naughty: "
        for j in range(len(naughty_kids)):
            if j == len(naughty_kids) - 1:
                final_result += f"{naughty_kids[j]}\n"
            else:
                final_result += f"{naughty_kids[j]}, "

    if not_found:
        final_result += "Not found: "
        for k in range(len(not_found)):
            if k == len(not_found) - 1:
                final_result += f"{not_found[k]}\n"
            else:
                final_result += f"{not_found[k]}, "

    return final_result[:-1]


def check_num(kids_list, num):
    result = 0
    kid = None

    for i in kids_list:
        if i[0] == int(num):
            result += 1
            kid = i
    if result == 1:
        return result, kid
    else:
        return None


def check_names(kids_list, name):
    result = 0
    kid = None

    for i in kids_list:
        if i[1] == name:
            result += 1
            kid = i
    if result == 1:
        return result, kid
    else:
        return None


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))



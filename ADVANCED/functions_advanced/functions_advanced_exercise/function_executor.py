def func_executor(*args):
    func_names = []
    numbers = []
    for i in args:
        func_names.append(i[0])
        numbers.append(i[1])

    result = ""
    for i in range(len(func_names)):
        func = func_names[i]
        nums = (numbers[i])
        result += func.__name__ + " - " + str(func(*nums)) + '\n'
    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

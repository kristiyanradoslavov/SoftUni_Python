# string = input()
# counter = int(input())
#
# repeat = lambda word, count: word * count
#
# result = repeat(string, counter)
# print(result)


string = input()
counter = int(input())


def repeater(param_to_repeat, times):
    result = param_to_repeat * times
    return result


print(repeater(string, counter))

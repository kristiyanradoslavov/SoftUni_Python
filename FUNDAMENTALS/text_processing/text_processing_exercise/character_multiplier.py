def calculations(first, second):
    result = 0
    for i in range(0, len(first)):
        result += ord(first[i]) * ord(second[i])
    return result


def remaining_calculations(first):
    result = 0
    for i in range(0, len(first)):
        result += ord(first[i])
    return result


all_strings = input().split(" ")

first_string = all_strings[0]
second_string = all_strings[1]

total_sum = 0

if len(first_string) > len(second_string):
    remaining_letters = first_string[len(second_string):]
    current_string = first_string[0:len(second_string)]
    total_sum += calculations(current_string, second_string)
    total_sum += remaining_calculations(remaining_letters)
elif len(first_string) < len(second_string):
    remaining_letters = second_string[len(first_string):]
    current_string = second_string[0:len(first_string)]
    total_sum += calculations(current_string, first_string)
    total_sum += remaining_calculations(remaining_letters)
else:
    total_sum += calculations(first_string, second_string)

print(total_sum)
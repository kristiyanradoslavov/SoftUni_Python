def sum_numbers(first, second):
    result = first + second
    return result


def subtract(sum, third):
    sum_result = sum - third
    return sum_result


def add_and_subtract(first, second, third):
    sum_of_first_two = sum_numbers(first, second)
    result = subtract(sum_of_first_two, third)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))


first_num = int(input())
second_num = int(input())
third_num = int(input())


def smallest_num(first, second, third):
    my_list = [first_num, second_num, third_num]
    smallest = min(my_list)
    return smallest


print(smallest_num(first_num, second_num, third_num))
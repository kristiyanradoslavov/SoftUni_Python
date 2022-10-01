def check_number(number):
    result = None
    divisor_list = []
    for num in range(number - 1, 0, -1):
        if number % num == 0:
            divisor_list.append(num)
    if sum(divisor_list) == number:
        result = "We have a perfect number!"
    else:
        result = "It's not so perfect."

    return result


number = int(input())
print(check_number(number))
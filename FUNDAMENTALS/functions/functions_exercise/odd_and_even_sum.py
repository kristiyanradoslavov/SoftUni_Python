def odd_and_even_numbers(number):
    str_to_int = str(number)
    odd_numbers = []
    even_numbers = []
    for num in range(0, len(str_to_int)):
        int_to_num = int(str_to_int[num])
        if int_to_num % 2 == 0:
            even_numbers.append(int_to_num)
        else:
            odd_numbers.append(int_to_num)
    total_odd = sum(odd_numbers)
    total_even = sum(even_numbers)

    result = f"Odd sum = {total_odd}, Even sum = {total_even}"
    return result


number = int(input())

print(odd_and_even_numbers(number))

numbers = list(map(int, input().split(', ')))

positive_nums = [check_1 for check_1 in numbers if check_1 >= 0]
negative_nums = [check_2 for check_2 in numbers if check_2 < 0]
even_nums = [check_3 for check_3 in numbers if check_3 % 2 == 0]
odd_nums = [check_4 for check_4 in numbers if check_4 % 2 != 0]

str_positive = list(map(lambda a: str(a), positive_nums))
str_negative = list(map(lambda a: str(a), negative_nums))
str_even = list(map(lambda a: str(a), even_nums))
str_odd = list(map(lambda a: str(a), odd_nums))

print(f"Positive: {', '.join(str_positive)}")
print(f"Negative: {', '.join(str_negative)}")
print(f"Even: {', '.join(str_even)}")
print(f"Odd: {', '.join(str_odd)}")


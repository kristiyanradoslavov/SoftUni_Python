numbers = input().split(' ')
int_numbers = []

for i in numbers:
    int_numbers.append(int(i))

min_num = min(int_numbers)
max_num = max(int_numbers)
sum_num = sum(int_numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")

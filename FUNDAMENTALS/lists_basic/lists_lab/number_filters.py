count_of_numbers = int(input())

all_numbers = []
final_list = []

for i in range(count_of_numbers):
    current_number = int(input())
    all_numbers.append(current_number)

command = input()

if command == "even":
    for num in all_numbers:
        if num % 2 == 0:
            final_list.append(num)
elif command == "odd":
    for num in all_numbers:
        if num % 2 != 0:
            final_list.append(num)
elif command == "negative":
    for num in all_numbers:
        if num < 0:
            final_list.append(num)
elif command == "positive":
    for num in all_numbers:
        if num >= 0:
            final_list.append(num)

print(final_list)
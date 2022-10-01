count_of_names = int(input())

odd_numbers = set()
even_numbers = set()

for index in range(1, count_of_names + 1):
    current_name = input()
    total_sum_of_letters = 0
    for letter in current_name:
        total_sum_of_letters += ord(letter)
    final_number = total_sum_of_letters // index
    if final_number % 2 == 0:
        even_numbers.add(final_number)
    else:
        odd_numbers.add(final_number)

odd_set_sum = sum(odd_numbers)
even_set_sum= sum(even_numbers)
final_set = set()

if odd_set_sum == even_set_sum:
    print(f"{odd_numbers.difference(even_numbers)}")
    final_set = odd_numbers.union(even_numbers)
elif odd_set_sum > even_set_sum:
    final_set = odd_numbers.difference(even_numbers)
elif even_set_sum > odd_set_sum:
    even_result = odd_numbers.symmetric_difference(even_numbers)
    final_set = even_result

for index, char in enumerate(final_set):
    if index != len(final_set) - 1:
        print(char, end=", ")
    else:
        print(char)
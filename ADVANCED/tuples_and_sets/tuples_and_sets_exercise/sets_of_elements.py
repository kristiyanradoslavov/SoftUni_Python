set_lengths = list(map(int, input().split()))
first_set_length = set_lengths[0]
second_set_length = set_lengths[1]

first_set = set()
second_set = set()

for first in range(first_set_length):
    first_input = int(input())
    first_set.add(first_input)

for second in range(second_set_length):
    second_input = int(input())
    second_set.add(second_input)

final_set = first_set.intersection(second_set)

for final in final_set:
    print(final)
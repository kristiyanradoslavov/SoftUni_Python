count_of_lines = int(input())

longest_set = {}


for index in range(count_of_lines):
    current_ranges = input().split("-")
    first_start, first_end = current_ranges[0].split(",")
    second_start, second_end = current_ranges[1].split(",")
    first_range = {x for x in range(int(first_start), int(first_end) + 1)}
    second_range = {y for y in range(int(second_start), int(second_end) + 1)}
    final_set = first_range.intersection(second_range)
    if len(longest_set) < len(final_set):
        longest_set.clear()
        longest_set = final_set

final_list = list(("".join(str(x)) for x in longest_set))

print(f'Longest intersection is {list(int(y) for y in final_list)} with length {len(longest_set)}')
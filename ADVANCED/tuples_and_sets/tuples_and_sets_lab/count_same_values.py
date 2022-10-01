all_numbers = tuple(map(float, input().split()))

all_nums_dict = {}

for current_num in all_numbers:
    if current_num in all_nums_dict:
        all_nums_dict[current_num] += 1
    else:
        all_nums_dict[current_num] = 1

for key, value in all_nums_dict.items():
    print(f"{key} - {value} times")

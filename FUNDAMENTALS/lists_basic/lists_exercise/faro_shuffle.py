cards = input()
shuffle_count = int(input())

first_list = cards.split()

final_list = []
current_index = -1
half_length = len(first_list)/2

start_list = first_list
finish_list = []

for shuffle_count in range(shuffle_count):
    for length in range(int(half_length)):
        current_index += 1
        for card in range(current_index, len(first_list), int(half_length)):
            finish_list.append(start_list[card])

    start_list = finish_list
    finish_list = []
    current_index = -1

print(start_list)





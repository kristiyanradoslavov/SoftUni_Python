number_string = input().split(', ')
beggars = int(input())

final_list = []
index = 0
num = 0


for count_of_beggars in range(beggars):
    for beggar in range(index, len(number_string), beggars):
        num += int((number_string[beggar]))

    final_list.append(num)
    num = 0
    index += 1

print(final_list)
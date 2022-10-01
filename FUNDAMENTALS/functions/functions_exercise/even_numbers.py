def numbers(num):
    if num % 2 == 0:
        return True
    return False


numbs = input().split(" ")

int_numbs = []

for i in numbs:
    int_numbs.append(int(i))

filtered_nums = filter(numbers, int_numbs)

even_list = list(filtered_nums)

print(even_list)


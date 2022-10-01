count_of_names = int(input())

name_set = set()

for _ in range(count_of_names):
    current_name = input()
    name_set.add(current_name)

for i in name_set:
    print(i)

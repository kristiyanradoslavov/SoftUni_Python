numbers = list(map(int,input().split(" ")))

average_num = sum(numbers) / len(numbers)

greater_list = [x for x in numbers if x > average_num]

top_five = []

for iteration in range(5):
    if greater_list == []:
        break
    max_num = max(greater_list)
    top_five.append(max_num)
    greater_list.remove(max_num)

if top_five != []:
    print(" ".join(str(a) for a in top_five))
else:
    print("No")
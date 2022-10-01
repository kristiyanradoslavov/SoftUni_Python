numbers = list(map(int, input().split(", ")))

final_num = 10

while numbers != []:
    current_list = []
    for num in numbers:
        if num <= final_num:
            current_list.append(num)
    for remove in current_list:
        numbers.remove(remove)
    print(f"Group of {final_num}'s: {current_list}")
    final_num += 10

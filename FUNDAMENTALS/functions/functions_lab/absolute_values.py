numbers = input().split(" ")

final_list = []
for i in numbers:
    final_list.append(abs(float(i)))

print(final_list)
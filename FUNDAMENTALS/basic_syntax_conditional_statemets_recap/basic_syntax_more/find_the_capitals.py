string = str(input())

final_list = list()

for i in range(len(string)):
    current_str = string[i]
    if current_str.isupper():
        final_list.append(i)


print(final_list)
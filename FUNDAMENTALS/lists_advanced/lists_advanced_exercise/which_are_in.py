filter_list = input().split(", ")
words_list = input().split(", ")

final_list = []
for check in filter_list:
    for second_check in words_list:
        if check in second_check:
            final_list.append(check)
            break

# result = (list(set(final_list)))
#
# print(sorted(list(result)))

print(final_list)
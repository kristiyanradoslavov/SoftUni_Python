string_input = input()

first_list = string_input.split()
final_list = []


# for i in first_list:          # работи директно по число или по съдържание на листа
for i in range(len(first_list)):  # работи по индекс
    num = int(first_list[i]) # vzima chisloto na vuprosniq index
    number = num * -1
    final_list.append(number)

print(final_list)



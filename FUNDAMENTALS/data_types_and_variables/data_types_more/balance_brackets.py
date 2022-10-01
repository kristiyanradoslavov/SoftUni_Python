count_of_rows = int(input())

bracket_list = []

for i in range(count_of_rows):
    current_input = input()
    if current_input == "(" or current_input == ")":
        bracket_list.append(current_input)

bracket_is_balanced = False

for j in range(0, len(bracket_list), 2):
    if len(bracket_list) % 2 == 0:
        if bracket_list[j] == "(" and bracket_list[j + 1] == ")":
            bracket_is_balanced = True
        else:
            bracket_is_balanced = False
            break

if bracket_is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

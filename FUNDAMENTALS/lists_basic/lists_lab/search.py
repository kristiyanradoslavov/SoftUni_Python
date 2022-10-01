number_of_inputs = int(input())
special_word = input()

all_inputs = []
clear_inputs = []

for i in range(number_of_inputs):
    current_strings = input()
    all_inputs.append(current_strings)
    if special_word in current_strings:
        clear_inputs.append(current_strings)

print(all_inputs)
print(clear_inputs)

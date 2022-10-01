sentence = input()

all_elements_dict = {}

for letter in sentence:
    if letter not in all_elements_dict:
        all_elements_dict[letter] = 0
    all_elements_dict[letter] += 1

for key, value in sorted(all_elements_dict.items()):
    print(f"{key}: {value} time/s")

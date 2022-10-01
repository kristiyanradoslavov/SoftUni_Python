command = input()
my_dict = {}
my_dict_check = {}

while ":" in command:
    current_command = command.split(":")
    key = current_command[0]
    value = current_command[1]
    value_2 = current_command[2]
    command = input()
    my_dict[key] = value
    my_dict_check[key] = value_2.lower()

word_check = command
if "_" in word_check:
    word_check = word_check.split("_")
    word_check = " ".join(word_check)

for i in my_dict_check:
    if my_dict_check[i] != word_check:
        del my_dict[i]

for key, value in my_dict.items():
    print(f"{key} - {value}")
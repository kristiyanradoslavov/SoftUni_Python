def add_func(command, word, numbers):
    if word == "Add":
        if command == "First":
            for i in numbers:
                first_sequence.add(int(i))
        elif command == "Second":
            for i in numbers:
                second_sequence.add(int(i))

    elif word == "Remove":
        if command == "First":
            for i in numbers:
                if int(i) in first_sequence:
                    first_sequence.remove(int(i))
        elif command == "Second":
            for i in numbers:
                if int(i) in second_sequence:
                    second_sequence.remove(int(i))


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
count_of_commands = int(input())

for _ in range(count_of_commands):
    current_command = input().split()
    control_word = current_command[0]

    if control_word == "Add":
        numbers_to_add = tuple(current_command[2:])
        add_func(current_command[1], control_word, numbers_to_add)

    elif control_word == "Remove":
        numbers_to_remove = tuple(current_command[2:])
        add_func(current_command[1], control_word, numbers_to_remove)

    elif control_word == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

for index, char in enumerate(sorted(first_sequence)):
    if index == len(first_sequence) - 1:
        print(char)
    else:
        print(char, end=", ")

for index, char in enumerate(sorted(second_sequence)):
    if index == len(second_sequence) - 1:
        print(char)
    else:
        print(char, end=", ")

def valid_index_check(first, second):
    result_is_valid = False
    if len(numb_sequence) > first > -1:
        if len(numb_sequence) > second > -1:
            if first != second:
                result_is_valid = True
    return result_is_valid


def check_for_hit(first, second):
    result = False
    if numb_sequence[first] == numb_sequence[second]:
        result = True
    return result


numb_sequence = input().split(" ")
command = input()
number_of_moves = 0


while command != "end":
    current_indexes = list(map(int, command.split(" ")))
    number_of_moves += 1
    half_length = int(len(numb_sequence) / 2)
    first_index = current_indexes[0]
    second_index = current_indexes[1]
    matching_element = ''

    if valid_index_check(first_index, second_index):
        if check_for_hit(first_index, second_index):
            matching_element = numb_sequence[first_index]
            numb_sequence.remove(matching_element)
            numb_sequence.remove(matching_element)
            # numb_sequence[first_index] = "k"
            # numb_sequence[second_index] = "k"
            # numb_sequence = list(filter(lambda a: a != "k", numb_sequence))
            print(f"Congrats! You have found matching elements - {matching_element}!")
            if numb_sequence == []:
                print(f"You have won in {number_of_moves} turns!")
                break
        else:
            print("Try again!")
    else:
        numb_sequence.insert(half_length, str(f"-{number_of_moves}a"))
        numb_sequence.insert(half_length, str(f"-{number_of_moves}a"))
        print("Invalid input! Adding additional elements to the board")

    command = input()

if command == "end" and numb_sequence != []:
    print("Sorry you lose :(")
    print(' '.join(numb_sequence))
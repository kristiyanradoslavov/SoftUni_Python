def add_piece(curr_piece, curr_composer, curr_key):
    result = False
    if curr_piece in piano_pieces_dict:
        print(f"{curr_piece} is already in the collection!")
    else:
        piano_pieces_dict[curr_piece] = {}
        piano_pieces_dict[curr_piece]["composer"] = curr_composer
        piano_pieces_dict[curr_piece]["key"] = curr_key
        result = True
    return result


def remove_piece(curr_piece):
    if curr_piece in piano_pieces_dict:
        del piano_pieces_dict[curr_piece]
        print(f"Successfully removed {curr_piece}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")


def change_piece(curr_piece, new_key):
    if curr_piece in piano_pieces_dict:
        piano_pieces_dict[curr_piece]["key"] = new_key
        print(f"Changed the key of {curr_piece} to {new_key}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")


count_of_pieces = int(input())

piano_pieces_dict = {}

for _ in range(count_of_pieces):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    add_piece(piece, composer, key)

command = input()

while command != "Stop":
    current_command = command.split("|")
    key_command = current_command[0]
    if key_command == "Add":
        piece_to_add = current_command[1]
        composer_to_add = current_command[2]
        key_to_add = current_command[3]
        if add_piece(piece_to_add, composer_to_add, key_to_add):
            print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")
    elif key_command == "Remove":
        piece_to_remove = current_command[1]
        remove_piece(piece_to_remove)
    elif key_command == "ChangeKey":
        piece_to_change = current_command[1]
        key_to_change = current_command[2]
        change_piece(piece_to_change,key_to_change)

    command = input()

for dict_key, dict_value in piano_pieces_dict.items():
    print(f"{dict_key} -> Composer: {dict_value['composer']}, Key: {dict_value['key']}")

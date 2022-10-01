encrypted_massage = input()
command = input()

while command != "Decode":
    current_command = command.split("|")
    key_command = current_command[0]
    if key_command == "Move":
        letters_to_move = int(current_command[1])
        letters = encrypted_massage[:letters_to_move]
        encrypted_massage = encrypted_massage[letters_to_move:] + letters
    elif key_command == "Insert":
        index_to_insert = int(current_command[1])
        value_to_insert = current_command[2]
        message = list(encrypted_massage)
        message.insert(index_to_insert, value_to_insert)
        encrypted_massage = "".join(message)
    elif key_command == "ChangeAll":
        old_string = current_command[1]
        new_string = current_command[2]
        encrypted_massage = encrypted_massage.replace(old_string, new_string)
    command = input()

print(f"The decrypted message is: {encrypted_massage}")
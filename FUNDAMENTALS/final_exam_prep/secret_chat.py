def insert_space(index):
    list_of_message = list(concealed_message)
    list_of_message.insert(index, " ")
    result = "".join(list_of_message)
    print(result)
    return result


def reverse(string_to_reverse):
    result = concealed_message
    if string_to_reverse in concealed_message:
        new_string = "".join(reversed(string_to_reverse))
        result = concealed_message.replace(string_to_reverse, "", 1)
        result += new_string
        print(result)
    else:
        print("error")
    return result


def change_all(old_string, new_string):
    result = concealed_message.replace(old_string, new_string)
    print(result)
    return result


concealed_message = input()

command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    key_command = current_command[0]
    if key_command == "InsertSpace":
        given_index = int(current_command[1])
        concealed_message = insert_space(given_index)
    elif key_command == "Reverse":
        substring = current_command[1]
        concealed_message = reverse(substring)
    elif key_command == "ChangeAll":
        old_text = current_command[1]
        new_text = current_command[2]
        concealed_message = change_all(old_text, new_text)
    command = input()

print(f"You have a new text message: {concealed_message}")
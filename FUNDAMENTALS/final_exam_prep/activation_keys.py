def containment(substring):
    if substring in raw_activation_key:
        print(f"{raw_activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip(command_to_flip, start, end):
    result = list(raw_activation_key)
    if command_to_flip == "Upper":
        for char in range(len(result)):
            if start <= char < end:
                str_to_replace = result[char].upper()
                result[char] = str_to_replace
        result = "".join(result)
        print(result)
    elif command_to_flip == "Lower":
        if command_to_flip == "Lower":
            for char_low in range(len(result)):
                if start <= char_low < end:
                    str_to_replace = result[char_low].lower()
                    result[char_low] = str_to_replace
            result = "".join(result)
            print(result)
    return result


def slice_func(start, end):
    result = raw_activation_key[:start] + raw_activation_key[end:]
    print(result)
    return result


raw_activation_key = input()

command = input()

while command != "Generate":
    current_command = command.split(">>>")
    key_word = current_command[0]

    if key_word == "Contains":
        sub_string = current_command[1]
        containment(sub_string)
    elif key_word == "Flip":
        flip_command = current_command[1]
        starting_index = int(current_command[2])
        end_index = int(current_command[3])
        raw_activation_key = flip(flip_command, starting_index, end_index)

    elif key_word == "Slice":
        start_slice = int(current_command[1])
        end_slice = int(current_command[2])
        raw_activation_key = slice_func(start_slice, end_slice)

    command = input()

print(f"Your activation key is: {raw_activation_key}")
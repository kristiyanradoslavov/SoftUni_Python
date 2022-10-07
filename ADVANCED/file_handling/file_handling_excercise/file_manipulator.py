from os import remove

command = input()

while command != "End":
    current_command = command.split("-")
    key_command = current_command[0]

    if key_command == "Create":
        file = open(f"./{current_command[1]}", "w")
        file.close()

    elif key_command == "Add":
        second_file = open(f"./{current_command[1]}", "a")
        second_file.write(f"{current_command[2]}\n")
        second_file.close()

    elif key_command == "Replace":
        try:
            third_file = open(f"./{current_command[1]}", "r")
            old_data = third_file.read()
            third_file.close()
            old_string = current_command[2]
            new_string = current_command[3]
            if old_string in old_data:
                third_file_to_write = open(f"./{current_command[1]}", "w")
                old_data = old_data.replace(old_string, new_string)
                third_file_to_write.write(old_data)
                third_file_to_write.close()

        except FileNotFoundError:
            print("An error occurred")

    elif key_command == "Delete":
        try:
            remove(f"./{current_command[1]}")

        except FileNotFoundError:
            print("An error occurred")

    command = input()
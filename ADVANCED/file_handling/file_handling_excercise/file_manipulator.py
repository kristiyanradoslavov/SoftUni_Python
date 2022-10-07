command = input()

while command != "End":
    current_command = command.split("-")
    key_command = current_command[0]

    if key_command == "Create":
        file = open(f"../files/{current_command[1]}", "a")
        file.close()

    elif key_command == "Add":
        second_file = open(f"../files/{current_command[1]}", "a")
        second_file.write(f"{current_command[2]}")
        second_file.close()

    elif key_command == "Replace":
        try:
            third_file = open(f"../{current_command[1]}", "r")
            third_file_for_writing = open(f"../{current_command[1]}", "w")
            old_string = current_command[2]
            new_string = current_command[3]
            if old_string in file.read():
                print("yes")

        except:
            print("An error occurred")


    elif key_command == "Delete":
        pass

    command = input()


def index_validation_check(index):
    check_is_ok = False
    if len(all_usernames) > index > -1:
        check_is_ok = True
    return check_is_ok


all_usernames = input().split(", ")
command = input()

blacklisted_count = 0
lost_names_count = 0

while command != "Report":
    current_command = command.split(" ")
    if current_command[0] == "Blacklist":
        comm = current_command[0]
        name = current_command[1]
        if name in all_usernames:
            blacklisted_count += 1
            for index, char in enumerate(all_usernames):
                if char == name:
                    all_usernames[index] = "Blacklisted"
                    print(f"{name} was blacklisted.")
                    break
        else:
            print(f"{name} was not found.")

    elif current_command[0] == "Error":
        index = int(current_command[1])
        if index_validation_check(index):
            if all_usernames[index] != "Blacklisted":
                if all_usernames[index] != "Lost":
                    print(f"{all_usernames[index]} was lost due to an error.")
                    lost_names_count += 1
                    all_usernames[index] = "Lost"

    elif current_command[0] == "Change":
        index = int(current_command[1])
        new_name = current_command[2]
        if index_validation_check(index):
            print(f"{all_usernames[index]} changed his username to {new_name}.")
            all_usernames[index] = new_name

    command = input()


print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_names_count}")
print(' '.join(all_usernames))

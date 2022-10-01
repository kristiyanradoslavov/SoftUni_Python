def check_if_phone_exists(phone_name):
    result = False
    if phone_name in list_of_phones:
        result = True
    return result


list_of_phones = input().split(", ")
command = input()

while command != "End":
    current_command = command.split(" - ")

    if current_command[0] == "Add":
        phone_info = current_command[1]
        if check_if_phone_exists(phone_info) is False:
            list_of_phones.append(phone_info)
    elif current_command[0] == "Remove":
        phone_info = current_command[1]
        if check_if_phone_exists(phone_info):
            list_of_phones.remove(phone_info)
    elif current_command[0] == "Bonus phone":
        phones = current_command[1].split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if check_if_phone_exists(old_phone):
            for index, char in enumerate(list_of_phones):
                if char == old_phone:
                    if index != len(list_of_phones) - 1:
                        list_of_phones.insert(index + 1, new_phone)
                        break
                    else:
                        list_of_phones.append(new_phone)
                        break
    elif current_command[0] == "Last":
        current_phone = current_command[1]
        if check_if_phone_exists(current_phone):
            list_of_phones.remove(current_phone)
            list_of_phones.append(current_phone)

    command = input()

print(', '.join(list_of_phones))
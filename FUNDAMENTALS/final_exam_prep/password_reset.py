def take_odd(pas_info):
    change_string = ""
    for char in range(0, len(pas_info)):
        if char % 2 != 0:
            change_string += pas_info[char]
    print(change_string)
    return change_string


def cut_string(pass_info, ind, leng):
    change_sting = ""
    change_sting += pass_info[:ind] + pass_info[ind + leng:]
    print(change_sting)
    return change_sting


def substitute_string(pass_info, old, new):
    final_string = pass_info
    if old in pass_info:
        final_string = final_string.replace(old, new)
        print(final_string)
    else:
        print("Nothing to replace!")
    return final_string


initial_password = input()

command = input()
new_password = initial_password

while command != "Done":
    current_command = command.split(" ")
    if current_command[0] == "TakeOdd":
        new_password = take_odd(new_password)
    elif current_command[0] == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
        new_password = cut_string(new_password,index,length)
    elif current_command[0] == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        new_password = substitute_string(new_password,substring,substitute)

    command = input()

print(f"Your password is: {new_password}")
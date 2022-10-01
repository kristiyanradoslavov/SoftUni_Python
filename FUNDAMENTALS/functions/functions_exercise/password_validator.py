def pass_check(password):
    length_check = False
    second_check = True
    digit_check = False
    digit_counter = 0

    if 6 <= len(password) <= 10:
        length_check = True

    for i in range(0, len(password)):
        char = ord(password[i])
        if (not 48 <= char <= 57) and (not 97 <= char <= 122):
            second_check = False
            break

    for i in range(0, len(password)):
        char = ord(password[i])
        if 48 <= char <= 57:
            digit_counter += 1

    if digit_counter >= 2:
        digit_check = True

    if length_check is False:
        print("Password must be between 6 and 10 characters")
    if second_check is False:
        print("Password must consist only of letters and digits")
    if digit_check is False:
        print("Password must have at least 2 digits")

    if length_check and second_check and digit_check:
        print("Password is valid")


input_pass = input().lower()
pass_check(input_pass)


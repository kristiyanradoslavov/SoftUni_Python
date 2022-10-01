def validation_check(username):
    if 3 <= len(username) <= 16:
        containment_check(username)


def containment_check(username):
    final_username = ""
    for letter in username:
        if letter.isdigit() or letter.isalpha() or letter == "_" or letter == "-":
            final_username += letter
        if len(final_username) == len(username):
            print(username)


usernames = input().split(", ")

for current_user in usernames:
    validation_check(current_user)
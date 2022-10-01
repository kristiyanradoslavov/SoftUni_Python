command = input()

all_users = {}

while command != "Lumpawaroo":
    if "|" in command:
        current_user = command.split(" | ")
        force_side = current_user[0]
        force_user = current_user[1]
        if force_side not in all_users:
            all_users[force_side] = []
        if force_user not in all_users.values():
            all_users[force_side].append(force_user)

    elif " > " in command:
        current_user = command.split(" > ")
        force_user = current_user[0]
        force_side = current_user[1]
        current_user_side = ""
        if force_user in all_users.values():
            all_users.values()



    command = input()
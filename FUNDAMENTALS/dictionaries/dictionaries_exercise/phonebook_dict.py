command = input()

my_dict = {}

while not command.isdigit():
    phone_info = command.split("-")
    name = phone_info[0]
    phone = phone_info[1]
    my_dict[name] = phone

    command = input()

num = int(command)

for i in range(num):
    name_to_search = input()
    if name_to_search in my_dict:
        print(f"{name_to_search} -> {my_dict[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")


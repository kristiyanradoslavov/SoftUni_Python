number_of_wagons = int(input())
command = input()
wagon_list = []

for wagons in range(number_of_wagons):
    wagon_list.append(int(0))


while command != "End":
    list_command = command.split(" ")
    if list_command[0] == "add":
        wagon_list[-1] += int(list_command[1])
    elif list_command[0] == "insert":
        wagon_list[int(list_command[1])] += int(list_command[2])
    elif list_command[0] == "leave":
        wagon_list[int(list_command[1])] -= int(list_command[2])

    command = input()

print(wagon_list)
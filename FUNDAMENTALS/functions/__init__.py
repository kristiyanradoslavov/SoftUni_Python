gifts_names = input().split()
command = input()
while command != "No Money":
    the_command = command.split()
    if the_command[0] == "OutOfStock":
        while the_command[1] in gifts_names:
            index = gifts_names.index(the_command[1])
            gifts_names[index] = "None"
    elif the_command[0] == "Required":
        if int(the_command[2]) <= len(gifts_names)-1:
            gifts_names[int(the_command[2])] = the_command[1]
    elif the_command[0] == "JustInCase":
        gifts_names[-1] = the_command[1]
    command = input()
while "None" in gifts_names:
    gifts_names.remove("None")
final_gifts = " ".join(gifts_names)
print(final_gifts)
import re
destination = input()
command = input()

while command != "Travel":
    current_command = command.split(":")
    first_command = current_command[0]
    second_command = current_command[1]
    third_command = current_command[2]
    if first_command == "Add Stop":
        if 0 <= int(second_command) < len(destination):
            destination = destination[0:int(second_command)] + third_command + destination[int(second_command):]
    elif first_command == "Remove Stop":
        if (0 <= int(second_command) < len(destination)) and (0 <= int(third_command) < len(destination)):
            # destination = destination[:int(second_command)] + destination[int(third_command) + 1:]
            destination = destination.replace(destination[int(second_command):int(third_command) + 1], "")
    elif first_command == "Switch":
        if second_command.lower() in destination.lower():
            result = re.findall(f"{second_command.lower()}",destination, re.IGNORECASE)
            destination = destination.replace(result[0], third_command)
    print(destination)
    command = input()

print(f"Ready for world tour! Planned stops: {destination}")

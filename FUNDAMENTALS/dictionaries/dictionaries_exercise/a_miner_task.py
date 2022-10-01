command = input()

resources = {}

while command != "stop":
    if command not in resources:
        resources[command] = []
        resources[command].append(int(input()))
    else:
        resources[command].append(int(input()))
    command = input()

for key, value in resources.items():
    print(f"{key} -> {sum(value)}")
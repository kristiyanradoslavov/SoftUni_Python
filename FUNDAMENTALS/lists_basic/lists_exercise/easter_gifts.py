gifts = input().split()
command = input().split(' ')


while command[0] != "No":
    if command[0] == "OutOfStock":
        for index, char in enumerate(gifts):
            if command[1] == char:
                gifts.remove(char)
                gifts.insert(index, "None")
    elif command[0] == "Required":
        for index, char in enumerate(gifts):
            if index == int(command[2]):
                gifts.pop(int(command[2]))
                gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        gifts.pop()
        gifts.append(command[1])

    command = input().split(" ")

for i in gifts:
    if i != "None":
        print(f"{i}", end=" ")

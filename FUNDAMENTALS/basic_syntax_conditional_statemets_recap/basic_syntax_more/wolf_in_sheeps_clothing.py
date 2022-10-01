flock = input().split(", ")

for index, char in enumerate(flock):
    if char == "wolf":
        if index + 1 == len(flock):
            print("Please go away and stop eating my sheep")
        else:
            current_position = len(flock) - index - 1
            print(f"Oi! Sheep number {current_position}! You are about to be eaten by a wolf!")

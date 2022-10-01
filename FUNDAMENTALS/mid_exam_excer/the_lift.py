people_waiting = int(input())
wagon_state = list(map(int, input().split()))

for index, char in enumerate(wagon_state):
    while wagon_state[index] < 4:
        if people_waiting == 0:
            break
        wagon_state[index] += 1
        people_waiting -= 1

Full_wagons = False
if wagon_state[-1] == 4:
    Full_wagons = True

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(str(x) for x in wagon_state))
elif people_waiting == 0 and Full_wagons:
    print(" ".join(str(x) for x in wagon_state))
elif people_waiting == 0:
    print("The lift has empty spots!")
    print(" ".join(str(x) for x in wagon_state))



from collections import deque


def check_if_zero():
    if chocolate_stack:
        while chocolate_stack[-1] <= 0:
            chocolate_stack.pop()
            if not chocolate_stack:
                break

    if cups_of_milk:
        while cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
            if not cups_of_milk:
                break


chocolate_stack = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

chocolate_milkshakes = 0

while chocolate_milkshakes < 5:
    check_if_zero()
    if (not cups_of_milk) or (not chocolate_stack):
        break
    current_chocolate = chocolate_stack.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate == current_cup_of_milk:
        chocolate_milkshakes += 1
    else:
        cups_of_milk.append(current_cup_of_milk)
        current_chocolate -= 5
        chocolate_stack.append(current_chocolate)

if chocolate_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print("Chocolate: ", end="")
    for i in range(len(chocolate_stack)):
        if i < len(chocolate_stack) - 1:
            print(chocolate_stack[i], end=", ")
        else:
            print(chocolate_stack[i])
else:
    print("Chocolate: empty")

if cups_of_milk:
    print("Milk: ", end="")
    for i in range(len(cups_of_milk)):
        if i < len(cups_of_milk) - 1:
            print(cups_of_milk[i], end=", ")
        else:
            print(cups_of_milk[i])
else:
    print("Milk: empty")


from collections import deque


def drop_off(symbol, bee, nectar):
    result = 0
    if symbol == "+":
        result = bee + nectar
    elif symbol == "-":
        result = bee - nectar
    elif symbol == "*":
        result = bee * nectar
    elif symbol == "/":
        if bee != 0:
            result = bee / nectar

    working_bees.popleft()
    nectar_stack.pop()
    symbols_deque.popleft()
    return abs(result)


working_bees = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))
symbols_deque = deque(input().split())

total_honey = 0

for i in range(len(working_bees)):
    if (not nectar_stack) or (not working_bees):
        break
    if nectar_stack[-1] >= working_bees[0]:
        total_honey += drop_off(symbols_deque[0], working_bees[0], nectar_stack[-1])
    else:
        nectar_stack.pop()
        while nectar_stack:
            if nectar_stack[-1] >= working_bees[0]:
                total_honey += drop_off(symbols_deque[0], working_bees[0], nectar_stack[-1])
                break
            else:
                nectar_stack.pop()


print(f"Total honey made: {total_honey}")
if working_bees:
    print("Bees left: ", end="")
    for i in range(len(working_bees)):
        if i == len(working_bees) - 1:
            print(working_bees[i])
        else:
            print(working_bees[i], end=", ")

if nectar_stack:
    print("Nectar left: ", end="")
    for j in range(len(nectar_stack)):
        if j == len(nectar_stack) - 1:
            print(nectar_stack[j])
        else:
            print(nectar_stack[j], end=", ")
count_of_nums = int(input())

stack = []

for command in range(count_of_nums):
    current_input = input().split()
    if len(current_input) > 1:
        num = int(current_input[1])
        stack.append(num)
    elif current_input[0] == "2":
        if stack:
            stack.pop()
    elif current_input[0] == "3":
        # if stack:
            print(max(stack))
    elif current_input[0] == "4":
        if stack:
            print(min(stack))


while stack:
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())

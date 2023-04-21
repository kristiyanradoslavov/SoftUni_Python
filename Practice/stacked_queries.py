n = int(input())
stack = []


for current_input in range(n):
    current_number = input().split(" ")

    if current_number[0] == "1":
        stack.append(current_number[1])

    elif current_number[0] == "2":
        if stack:
            stack.pop()

    elif current_number[0] == "3":
        if stack:
            max_number = max(stack)
            print(max_number)

    elif current_number[0] == "4":
        if stack:
            min_number = min(stack)
            print(min_number)

print(", ".join(stack[::-1]))

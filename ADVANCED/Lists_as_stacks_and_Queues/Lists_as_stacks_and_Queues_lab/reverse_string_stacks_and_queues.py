current_input = input()
first_list = [x for x in current_input]
stack = []

for _ in range(len(first_list)):
    stack.append(first_list.pop())

print("".join(stack))
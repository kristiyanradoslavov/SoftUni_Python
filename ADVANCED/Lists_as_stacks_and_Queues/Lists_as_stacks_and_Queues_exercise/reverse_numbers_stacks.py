stack = input().split(" ")

new_stack = []

while stack:
    current_num = stack.pop()
    new_stack.append(current_num)

print(" ".join(new_stack))
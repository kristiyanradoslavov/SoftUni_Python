numbers = input().split(" ")

stack = []

while numbers:
    current_num = numbers.pop()
    stack.append(current_num)


print(" ".join(stack))
math_expression = input()

stack = []
for char in range(len(math_expression)):
    if math_expression[char] == "(":
        stack.append(int(char))
    elif math_expression[char] == ")":
        stack.append(int(char))
        final_index = stack.pop()
        first_index = stack.pop()
        print(math_expression[first_index:final_index + 1])
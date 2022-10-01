def operate(operator, *args):
    def add():
        result = 0
        for i in args:
            result += i
        return result

    def subtract():
        result = 0
        for i in range(len(args)):
            if i == 0:
                result = args[i]
            else:
                result -= args[i]
        return result

    def multiply():
        result = 1
        for i in args:
            result *= i
        return result

    def divide():
        result = 0
        for i in range(len(args)):
            if i == 0:
                result = args[i]
            else:
                result /= args[i]
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("/", 10, 2))

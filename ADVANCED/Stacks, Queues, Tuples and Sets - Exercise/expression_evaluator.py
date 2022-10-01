from collections import deque
from math import floor
import re


def division(symbol):
    result = 0
    while current_deque:
        if symbol == "-":
            if result == 0:
                result += current_deque.popleft() - current_deque.popleft()
            else:
                result -= current_deque.popleft()
        elif symbol == "+":
            if result == 0:
                result += current_deque.popleft() + current_deque.popleft()
            else:
                result += current_deque.popleft()
        elif symbol == "/":
            if result == 0:
                result = floor(current_deque.popleft() / current_deque.popleft())
            else:
                result = floor(result / current_deque.popleft())
        elif symbol == "*":
            if result == 0:
                result = current_deque.popleft() * current_deque.popleft()
            else:
                result *= current_deque.popleft()

    return result


expression = deque(input().split())

current_deque = deque()

while expression:
    current_symbol = expression.popleft()
    if re.match("[+-]?\d", current_symbol):
        current_deque.append(int(current_symbol))
    elif not current_symbol.isdigit():
        if current_symbol == "*":
            current_deque.append(division(current_symbol))
        elif current_symbol == "-":
            current_deque.append(division(current_symbol))
        elif current_symbol == "+":
            current_deque.append(division(current_symbol))
        elif current_symbol == "/":
            current_deque.append(division(current_symbol))

for i in current_deque:
    print(i)

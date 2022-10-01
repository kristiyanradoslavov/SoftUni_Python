from collections import deque

rows, cols = [int(x) for x in input().split()]
snake_string = input()

final_index = 0

matrix = deque()

for i in range(rows):
    matrix.append(deque())

control_word = deque(snake_string)

for j in range(len(matrix)):
    if j % 2 == 0:
        for k in range(cols):
            if control_word:
                matrix[j].append(control_word.popleft())
            else:
                control_word = deque(snake_string)
                matrix[j].append(control_word.popleft())

    else:
        for k in range(cols - 1, -1, -1):
            if control_word:
                matrix[j].appendleft(control_word.popleft())
            else:
                control_word = deque(snake_string)
                matrix[j].appendleft(control_word.popleft())

for i in range(len(matrix)):
    print("".join(matrix[i]))
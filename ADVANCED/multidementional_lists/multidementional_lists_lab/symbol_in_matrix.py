cols = int(input())

matrix = []
for i in range(cols):
    matrix.append([])
    row = input()
    for j in row:
        matrix[i].append(j)

symbol = input()
special_symbol_found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            special_symbol_found = True
            break
    if special_symbol_found:
        break

if not special_symbol_found:
    print(f"{symbol} does not occur in the matrix")

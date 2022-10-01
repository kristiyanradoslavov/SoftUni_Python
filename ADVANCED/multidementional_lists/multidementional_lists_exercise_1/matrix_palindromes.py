row, col = [int(x) for x in input().split()]

first_and_last = []

for j in range(row):
    first_and_last.append([])
    current_letter = chr(97 + j)
    for i in range(col):
        first_and_last[j].append([])
        first_and_last[j][i].append(current_letter)
        first_and_last[j][i].append(chr(97 + i + j))
        first_and_last[j][i].append(current_letter)


for i in range(len(first_and_last)):
    for j in range(len(first_and_last[i])):
        print("".join(first_and_last[i][j]), end=" ")
    print()
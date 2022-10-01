rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    col = input().split()
    matrix.append(col)

counter = 0

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        first_result = matrix[i][j:j + 2]
        second_result = matrix[i + 1][j:j + 2]
        final_result = first_result + second_result
        check_list = []
        for k in range(len(final_result)):
            if k == 0:
                check_list.append(final_result[k])
            if check_list[0] != final_result[k]:
                break
            if k == len(final_result) -1:
                if check_list[0] == final_result[k]:
                    counter += 1

print(counter)
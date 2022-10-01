first_num = int(input())

counter = 0
for i in range(first_num, 0, -1):
    result = first_num % i
    if result == 0:
        counter += 1
if counter == 2:
    print("True")
else:
    print("False")
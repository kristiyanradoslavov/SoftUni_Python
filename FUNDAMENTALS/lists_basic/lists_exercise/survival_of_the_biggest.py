import sys
numbers = input().split()
count_to_remove = int(input())

int_numbers = []

for i in numbers:
    int_numbers.append(int(i))

for count in range(1, count_to_remove + 1):
    num_to_remove = sys.maxsize
    for num in int_numbers:
        if num < num_to_remove:
            num_to_remove = num
    int_numbers.remove(num_to_remove)

for k in range(0, len(int_numbers)):
    if k < len(int_numbers) - 1:
        print(f"{int_numbers[k]}", end=", ")
    elif k == len(int_numbers) - 1:
        print(f"{int_numbers[k]}")


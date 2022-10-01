def factorial(current_num):
    all_factorials = []
    for num in range(current_num, 0, -1):
        all_factorials.append(num)
    print(all_factorials)


first_num = int(input())
second_num = int(input())

factorial(first_num)